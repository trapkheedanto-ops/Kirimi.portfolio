#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Stage 2: logo, security (esc + rel attrs), Meru deep-dive section, expandable rich cards."""
P = "/workspace/Fortuna Labs/east-africa-heritage.html"
src = open(P, encoding="utf-8").read()
orig_len = len(src)

def sub_once(old, new, label):
    global src
    assert src.count(old) == 1, "AMBIGUOUS/MISSING: %s (count=%d)" % (label, src.count(old))
    src = src.replace(old, new)
    print("ok:", label)

# ── 1. MERU-CULTURAL LOGO (Kirinyaga peak + nguri horn + red soil, gold) ──
sub_once(
'''        <a class="brand" href="index.html">🗺️ East Africa Heritage<small>Mandoto na Urithi · Living Atlas</small></a>''',
'''        <a class="brand" href="index.html"><svg class="brand-mark" width="30" height="30" viewBox="0 0 40 40" aria-hidden="true" focusable="false">
                <circle cx="20" cy="20" r="19" fill="#3d1f12" stroke="#c9a24b" stroke-width="1.6"/>
                <path d="M7 30 L15.5 12.5 L20 21.5 L24.5 10.5 L33 30 Z" fill="#c9a24b"/>
                <path d="M15.5 12.5 L18 17.8 L13.6 17.8 Z M24.5 10.5 L27.2 16.2 L22.4 16.2 Z" fill="#fdf6e3"/>
                <rect x="7" y="30" width="26" height="3.6" rx="1.2" fill="#8a3b1e"/>
                <path d="M11.5 27.5 Q20 32.5 28.5 27.5" fill="none" stroke="#f4d58d" stroke-width="1.6" stroke-linecap="round"/>
            </svg>East Africa Heritage<small>Mandoto na Urithi · Living Atlas</small></a>''',
"logo swap")

sub_once(
'''        .brand { font-family: 'Playfair Display', serif; font-weight: 800; font-size: 1.3rem; color: var(--gold-bright); letter-spacing: 0.5px; }''',
'''        .brand { font-family: 'Playfair Display', serif; font-weight: 800; font-size: 1.3rem; color: var(--gold-bright); letter-spacing: 0.5px; display: flex; align-items: center; gap: 10px; }
        .brand-mark { flex-shrink: 0; filter: drop-shadow(0 2px 6px rgba(201,162,75,.35)); }''',
"brand css")

# ── 2. SECURITY: esc() helper + escaping in innerHTML templates ──
sub_once(
'''    // ── HOME BASE: Meru, Kenya ─────────────────────────────
    var HOME = { name: "Meru, Kenya", lat: 0.35, lon: 37.5 };''',
'''    // ── HOME BASE: Meru, Kenya ─────────────────────────────
    var HOME = { name: "Meru, Kenya", lat: 0.35, lon: 37.5 };

    // ── SECURITY HELPERS ───────────────────────────────────
    // Every data value interpolated into HTML is escaped first (defence in depth
    // against injection through the atlas dataset or future user-supplied content).
    function esc(v) {
        return String(v === null || v === undefined ? "" : v)
            .replace(/&/g, "&amp;").replace(/</g, "&lt;").replace(/>/g, "&gt;")
            .replace(/"/g, "&quot;").replace(/'/g, "&#39;");
    }
    // Only http(s) links from the dataset are allowed to render as anchors.
    function safeHref(u) {
        return /^(https?:\\/\\/)[^"'<>\\\s]+$/i.test(u) ? u : null;
    }''',
"esc/safeHref helpers")

sub_once(
'''            title.textContent = s.flag + " " + s.name + " — " + s.country;''',
'''            title.textContent = s.flag + " " + s.name + " — " + s.country;''',
"title noop") if False else None

# card.innerHTML block -> escaped + details panel
sub_once(
'''            card.innerHTML =
                '<div class="card-top"><h3>' + s.flag + " " + s.name + '</h3><span class="coords">' +
                s.lat.toFixed(2) + "°, " + s.lon.toFixed(2) + "°</span></div>" +
                '<div class="badges">' + badges + "</div>" +
                '<div class="era-line">' + s.era + "</div>" +
                '<p class="desc">' + s.desc + "</p>" +
                '<div class="tags">' + s.tags.map(function (t) { return '<span class="tag">' + t + "</span>"; }).join("") + "</div>";''',
'''            card.innerHTML =
                '<div class="card-top"><h3>' + esc(s.flag) + " " + esc(s.name) + '</h3><span class="coords">' +
                s.lat.toFixed(2) + "°, " + s.lon.toFixed(2) + "°</span></div>" +
                '<div class="badges">' + badges + "</div>" +
                '<div class="era-line">' + esc(s.era) + "</div>" +
                '<p class="desc">' + esc(s.desc) + "</p>" +
                '<div class="tags">' + s.tags.map(function (t) { return '<span class="tag">' + esc(t) + "</span>"; }).join("") + "</div>" +
                detailPanel(s);''',
"card template escaping")

sub_once(
'''                         '<span class="badge dist">📍 ' + fmtKm(s._km) + " from " + origin.name.split(",")[0] + "</span>";''',
'''                         '<span class="badge dist">📍 ' + fmtKm(s._km) + " from " + esc(origin.name.split(",")[0]) + "</span>";''',
"badge escaping")

# empty-note & locate notes already static strings; keep. Add detailPanel + timeline escaping.
sub_once(
'''    // ── events ─────────────────────────────────────────────''',
'''    // ── expandable scholarly panel per card ────────────────
    function detailPanel(s) {
        var rows = [];
        if (s.lang)       rows.push('<div class="dp-row"><b>Languages:</b> ' + esc(s.lang) + "</div>");
        if (s.pop)        rows.push('<div class="dp-row"><b>Population / location:</b> ' + esc(s.pop) + "</div>");
        if (s.history)    rows.push('<div class="dp-row"><b>History:</b> ' + esc(s.history) + "</div>");
        if (s.art)        rows.push('<div class="dp-row"><b>Art & material culture:</b> ' + esc(s.art) + "</div>");
        if (s.traditions) rows.push('<div class="dp-row"><b>Living traditions:</b> ' + esc(s.traditions) + "</div>");
        if (s.economy)    rows.push('<div class="dp-row"><b>Economy then & now:</b> ' + esc(s.economy) + "</div>");
        if (s.links && s.links.length) {
            rows.push('<div class="dp-row"><b>Connections:</b><ul class="dp-links">' + s.links.map(function (l) {
                return "<li>[" + esc(l.type) + "] → " + esc(l.to) + ": " + esc(l.ev) + "</li>";
            }).join("") + "</ul></div>");
        }
        if (s.sources)    rows.push('<div class="dp-row dp-src"><b>Sources:</b> ' + esc(s.sources) + "</div>");
        if (s.refs && s.refs.length) {
            var refs = s.refs.map(function (u) {
                var h = safeHref(u);
                return h ? '<a href="' + esc(h) + '" target="_blank" rel="noopener noreferrer nofollow">' + esc(h) + "</a>" : "";
            }).filter(Boolean).join(" · ");
            if (refs) rows.push('<div class="dp-row dp-src"><b>Further reading:</b> ' + refs + "</div>");
        }
        if (!rows.length) return "";
        return '<details class="dp"><summary>📖 Full record — history, art, economy, connections & sources</summary><div class="dp-body">' + rows.join("") + "</div></details>";
    }

    // ── events ─────────────────────────────────────────────''',
"detailPanel fn")

print("stage2 part A ok")
open(P, "w", encoding="utf-8").write(src)
print("size:", len(src), "(was", orig_len, ")")
