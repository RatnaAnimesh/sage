module.exports = {
    stylesheet: [
        'https://cdn.jsdelivr.net/npm/katex@0.16.8/dist/katex.min.css'
    ],
    pdf_options: {
        "format": "Letter",
        "margin": {
            "top": "20mm",
            "right": "20mm",
            "bottom": "20mm",
            "left": "20mm"
        },
        "displayHeaderFooter": false
    },
    script: [
        { url: 'https://cdn.jsdelivr.net/npm/katex@0.16.8/dist/katex.min.js' },
        { url: 'https://cdn.jsdelivr.net/npm/katex@0.16.8/dist/contrib/auto-render.min.js' }
    ],
    body_class: ['markdown-body'],
    marked_options: {
        headerIds: false,
        smartypants: true,
    },
    options: {
        css: `
            .katex { font-size: 1.1em; }
        `
    }
};
