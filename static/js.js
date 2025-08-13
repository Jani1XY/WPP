async function getWiki() {
    console.log("RUNNING")
    bannderDiv = document.getElementById("bannerDiv")
    const url = 'http://localhost:2021/banners';

    try {
        const response = await fetch(url);

        if (!response.ok) {
            throw new Error(`Response status: ${response.status}`);
        }

        console.log(response);
        r = await response.json()
        console.log("Server üzeni: "+r.message)
        htmlText = r.div
        
    } catch (error) {
        console.error(error.message);
    }
    
    // const parser = new DOMParser();
    // const wiki = parser.parseFromString(htmlText, 'text/html');
    
    // banners = wiki.querySelector("div.tabs-content.tabs-content-2")
    // console.log(banners)

    bannderDiv.innerHTML = htmlText
    bannderDiv.style.visibility = "visible"
}
