// Meeting Prep Capture popup logic.
// Flow: inject a scraper into the active tab, prefill the form, then build a
// handoff packet and copy it for the surface the user is pasting into.

// Holds the raw profile text captured from the page, kept out of the form so
// the user edits identity fields without seeing a wall of scraped text.
let capturedProfileText = "";

// This function is serialized and run in the page context, so it must be fully
// self-contained (no references to anything outside its own body).
function scrapePage() {
  const url = location.href;
  const isProfile = /https?:\/\/([\w.]*\.)?linkedin\.com\/in\//.test(url);

  if (isProfile) {
    const name = (document.querySelector("h1")?.innerText || "").trim();
    const headline = (
      document.querySelector("div.text-body-medium.break-words")?.innerText ||
      document.querySelector(".text-body-medium")?.innerText ||
      ""
    ).trim();

    // "Title at Company" is the common headline shape; split on it when present.
    let title = headline;
    let company = "";
    const atMatch = headline.match(/\s+at\s+(.+)$/i);
    if (atMatch) {
      company = atMatch[1].trim();
      title = headline.slice(0, atMatch.index).trim();
    }

    const main = document.querySelector("main");
    let profileText = (main ? main.innerText : document.body.innerText) || "";
    profileText = profileText.replace(/\n{3,}/g, "\n\n").trim().slice(0, 6000);

    return { type: "profile", name, title, company, companyUrl: "", profileText, pageUrl: url };
  }

  // Generic / company page: best-effort company name from metadata or title.
  const company = (
    document.querySelector('meta[property="og:site_name"]')?.content ||
    document.title.split("|")[0].split(" - ")[0] ||
    ""
  ).trim();

  return { type: "company", name: "", title: "", company, companyUrl: location.origin, profileText: "", pageUrl: url };
}

function setField(id, value) {
  if (value) document.getElementById(id).value = value;
}

async function init() {
  const status = document.getElementById("status");
  try {
    const [tab] = await chrome.tabs.query({ active: true, currentWindow: true });
    const [{ result }] = await chrome.scripting.executeScript({
      target: { tabId: tab.id },
      func: scrapePage,
    });

    if (result) {
      setField("name", result.name);
      setField("title", result.title);
      setField("company", result.company);
      setField("companyUrl", result.companyUrl);
      capturedProfileText = result.profileText || "";
      document.getElementById("pagetype").textContent =
        result.type === "profile"
          ? "Captured a LinkedIn profile."
          : "Captured a company / web page. Add the stakeholder by hand.";
    }
  } catch (err) {
    status.style.color = "#b00020";
    status.textContent = "Could not read this page. Fill the fields by hand.";
  }
}

function buildPacket() {
  const name = document.getElementById("name").value.trim();
  const title = document.getElementById("title").value.trim();
  const company = document.getElementById("company").value.trim();
  const companyUrl = document.getElementById("companyUrl").value.trim();
  const meetingType = document.getElementById("meetingType").value.trim();
  const date = document.getElementById("date").value.trim();

  const lines = [];
  // Explicit intent line first: the trigger test showed a bare profile drops to
  // medium-confidence routing, so always state the upcoming meeting outright.
  lines.push("Prep me for an upcoming meeting.");
  lines.push("");
  if (name) lines.push("Stakeholder: " + name + (title ? ", " + title : ""));
  else if (title) lines.push("Stakeholder title: " + title);
  lines.push("Company: " + (company || "(not specified)") + (companyUrl ? " (" + companyUrl + ")" : ""));
  lines.push("Meeting type: " + (meetingType || "not specified"));
  lines.push("Date: " + (date || "not specified"));

  if (capturedProfileText) {
    lines.push("");
    lines.push("--- Captured LinkedIn profile (analyze as the stakeholder profile) ---");
    lines.push(capturedProfileText);
  }

  return lines.join("\n");
}

// Where the handoff lands. The plugin only runs inside Claude Code and Cowork,
// so those just copy: you paste into a session that is already open, no tab to
// launch. Claude.ai web cannot run the plugin, so it is offered only as an
// explicitly labeled lite path, never as the silent default it used to be.
const SURFACES = {
  "claude-code": {
    open: null,
    color: "#2e7d32",
    status: "Copied. Paste into your Claude Code session, where the plugin runs.",
  },
  cowork: {
    open: null,
    color: "#2e7d32",
    status: "Copied. Paste into your Cowork session, where the plugin runs.",
  },
  web: {
    open: "https://claude.ai/new",
    color: "#b06a00",
    status:
      "Copied, opening claude.ai. The plugin does not run here, so this is a lighter prep. Install it in Claude Code or Cowork for the full brief and one-pager.",
  },
};

async function copyHandoff() {
  const status = document.getElementById("status");
  const surface = SURFACES[document.getElementById("surface").value] || SURFACES["claude-code"];
  try {
    await navigator.clipboard.writeText(buildPacket());
    status.style.color = surface.color;
    status.textContent = surface.status;
    if (surface.open) {
      await chrome.tabs.create({ url: surface.open });
    }
  } catch (err) {
    status.style.color = "#b00020";
    status.textContent = "Copy failed: " + err.message;
  }
}

document.getElementById("copyBtn").addEventListener("click", copyHandoff);

init();
