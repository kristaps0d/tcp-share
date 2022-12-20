function sleep(ms) {
    return new Promise(resolve => setTimeout(resolve, ms));
}

function findFaviconLink() {
    return document.getElementById('favicon')
}

function getFaviconUrl(id) {
    return `/static/images/favicons/frame${id}.png`
}

async function animation() {
    let favObj = findFaviconLink();
    let state = 1;

    while (1) {
        // State counter
        state ++;
        if (state > 24) {
            state = 0;
        }

        favObj.setAttribute('href', getFaviconUrl(state))
        await sleep(100)
    }
}

animation();