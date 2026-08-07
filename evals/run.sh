#!/usr/bin/env bash
#
# Researcher-subagent regression harness.
#
# Stopgap for `claude plugin eval`, which is gated behind early access as of
# Claude Code 2.1.223. See README.md for the migration path.
#
# Each case spawns one researcher subagent headlessly against a fixed target
# with documented ground truth, then asserts on the returned dossier:
#   required_patterns   must all be present
#   forbidden_patterns  must all be absent
#   must_flag           a known fabrication that must appear somewhere, meaning
#                       the agent surfaced and labeled it rather than silently
#                       carrying it as fact
#
# Usage:
#   ./run.sh                 run every case
#   ./run.sh <case-id> ...   run named cases only
#   ./run.sh --list          list case ids and their cost, run nothing
#
# Env:
#   EVAL_MODEL      passed to claude --model (default: session default)
#   EVAL_TIMEOUT    per-case seconds (default: 900)
#
# Exit: 0 all passed, 1 any failed, 2 setup problem.

set -uo pipefail

HERE="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
CASE_DIR="$HERE/cases"
RUN_STAMP="$(date +%Y%m%d-%H%M%S)"
OUT_DIR="$HERE/results/$RUN_STAMP"
TIMEOUT="${EVAL_TIMEOUT:-900}"

command -v claude >/dev/null 2>&1 || { echo "ERROR: claude not on PATH" >&2; exit 2; }
command -v jq     >/dev/null 2>&1 || { echo "ERROR: jq not on PATH" >&2; exit 2; }
[ -d "$CASE_DIR" ]                || { echo "ERROR: no cases/ dir at $CASE_DIR" >&2; exit 2; }

if [ "${1:-}" = "--list" ]; then
  for f in "$CASE_DIR"/*.json; do
    printf "%-42s %s\n" "$(jq -r .id "$f")" "$(jq -r .cost_note "$f")"
  done
  exit 0
fi

# Select cases.
FILES=()
if [ $# -gt 0 ]; then
  for want in "$@"; do
    f="$CASE_DIR/$want.json"
    [ -f "$f" ] || { echo "ERROR: no such case: $want" >&2; exit 2; }
    FILES+=("$f")
  done
else
  for f in "$CASE_DIR"/*.json; do FILES+=("$f"); done
fi

[ ${#FILES[@]} -gt 0 ] || { echo "ERROR: no cases found in $CASE_DIR" >&2; exit 2; }

mkdir -p "$OUT_DIR"
echo "Researcher regression harness"
echo "  cases:   ${#FILES[@]}"
echo "  results: $OUT_DIR"
echo "  note:    each case makes real web searches and costs real tokens"
echo

TOTAL_FAIL=0
SUMMARY=""

for f in "${FILES[@]}"; do
  ID=$(jq -r .id "$f")
  AGENT=$(jq -r .agent "$f")
  PROMPT=$(jq -r .prompt "$f")
  RAW="$OUT_DIR/$ID.md"

  echo "── $ID"
  echo "   agent: $AGENT"

  # Ask the headless session to spawn exactly this subagent and return its
  # dossier verbatim. The subagent's own tools come from its frontmatter.
  DRIVER="Use the Task tool to spawn exactly one subagent of type '$AGENT'. Pass it this task prompt verbatim, changing nothing:

---
$PROMPT
---

When it returns, output its response verbatim and nothing else. Do not summarize, reformat, add a preamble, or comment on it."

  # bash 3.2 (macOS default) treats "${arr[@]}" on an empty array as unbound
  # under `set -u`, so branch instead of expanding a possibly-empty array.
  START=$(date +%s)
  if [ -n "${EVAL_MODEL:-}" ]; then
    timeout "$TIMEOUT" claude -p "$DRIVER" \
      --allowedTools "Task,WebSearch,WebFetch" \
      --model "$EVAL_MODEL" > "$RAW" 2>"$OUT_DIR/$ID.stderr"
  else
    timeout "$TIMEOUT" claude -p "$DRIVER" \
      --allowedTools "Task,WebSearch,WebFetch" > "$RAW" 2>"$OUT_DIR/$ID.stderr"
  fi
  RC=$?
  ELAPSED=$(( $(date +%s) - START ))

  if [ $RC -ne 0 ]; then
    echo "   RESULT: ERROR (exit $RC after ${ELAPSED}s) — see $ID.stderr"
    SUMMARY+="ERROR  $ID (exit $RC)\n"
    TOTAL_FAIL=$((TOTAL_FAIL + 1))
    echo
    continue
  fi

  if [ ! -s "$RAW" ]; then
    echo "   RESULT: ERROR (empty output after ${ELAPSED}s)"
    SUMMARY+="ERROR  $ID (empty output)\n"
    TOTAL_FAIL=$((TOTAL_FAIL + 1))
    echo
    continue
  fi

  CASE_FAIL=0

  assert_group() {
    local group="$1" expect="$2" label="$3" n
    n=$(jq -r ".assert.$group | length" "$f")
    [ "$n" = "0" ] && return 0
    for i in $(seq 0 $((n - 1))); do
      local name pat hit
      name=$(jq -r ".assert.$group[$i].name" "$f")
      pat=$(jq -r ".assert.$group[$i].pattern" "$f")
      if grep -qE "$pat" "$RAW"; then hit=yes; else hit=no; fi
      if [ "$hit" = "$expect" ]; then
        printf "   PASS  %s: %s\n" "$label" "$name"
      else
        printf "   FAIL  %s: %s  (/%s/)\n" "$label" "$name" "$pat"
        CASE_FAIL=$((CASE_FAIL + 1))
      fi
    done
  }

  assert_group required_patterns  yes "required "
  assert_group forbidden_patterns no  "forbidden"
  assert_group must_flag          yes "flagged  "

  if [ $CASE_FAIL -eq 0 ]; then
    echo "   RESULT: PASS (${ELAPSED}s, $(wc -l < "$RAW" | tr -d ' ') lines)"
    SUMMARY+="PASS   $ID (${ELAPSED}s)\n"
  else
    echo "   RESULT: FAIL ($CASE_FAIL assertion(s), ${ELAPSED}s) — see $ID.md"
    SUMMARY+="FAIL   $ID ($CASE_FAIL assertions)\n"
    TOTAL_FAIL=$((TOTAL_FAIL + 1))
  fi
  echo
done

echo "══ Summary"
printf "%b" "$SUMMARY"
echo
echo "Dossiers: $OUT_DIR"

if [ $TOTAL_FAIL -eq 0 ]; then
  echo "All cases passed."
  exit 0
fi
echo "$TOTAL_FAIL case(s) failed."
exit 1
