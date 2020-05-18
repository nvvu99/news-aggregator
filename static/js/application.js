// const articles = {
//     'header': 'Today',
//     'list': [
//         {
//             'thumb': '',
//             'title': `Google confirm EA games coming to Stadia, PlayerUnknown's Battlegrounds out now and free for Pro`,
//             'sapo': `Today Google did a new Stadia Connect video for their gaming service, which was pre-recorded due to the ongoing Coronavirus situation. Google confirmed a bunch more games coming including from EA, PlayerUnknown's Battlegrounds is out now and more. What is Stadia? Stadia is Google's game streaming service powered by Linux and Vulkan. You can play games in a Chromium browser on a Linux desktop. It'`,
//             'publisher_name': `GamingOnLinux`,
//         },
//         {
//             'thumb': '',
//             'title': `Google confirm EA games coming to Stadia, PlayerUnknown's Battlegrounds out now and free for Pro`,
//             'sapo': `Today Google did a new Stadia Connect video for their gaming service, which was pre-recorded due to the ongoing Coronavirus situation. Google confirmed a bunch more games coming including from EA, PlayerUnknown's Battlegrounds is out now and more. What is Stadia? Stadia is Google's game streaming service powered by Linux and Vulkan. You can play games in a Chromium browser on a Linux desktop. It'`,
//             'publisher_name': `GamingOnLinux`,
//         },
//         {
//             'thumb': '',
//             'title': `Google confirm EA games coming to Stadia, PlayerUnknown's Battlegrounds out now and free for Pro`,
//             'sapo': `Today Google did a new Stadia Connect video for their gaming service, which was pre-recorded due to the ongoing Coronavirus situation. Google confirmed a bunch more games coming including from EA, PlayerUnknown's Battlegrounds is out now and more. What is Stadia? Stadia is Google's game streaming service powered by Linux and Vulkan. You can play games in a Chromium browser on a Linux desktop. It'`,
//             'publisher_name': `GamingOnLinux`,
//         },
//         {
//             'thumb': '',
//             'title': `Google confirm EA games coming to Stadia, PlayerUnknown's Battlegrounds out now and free for Pro`,
//             'sapo': `Today Google did a new Stadia Connect video for their gaming service, which was pre-recorded due to the ongoing Coronavirus situation. Google confirmed a bunch more games coming including from EA, PlayerUnknown's Battlegrounds is out now and more. What is Stadia? Stadia is Google's game streaming service powered by Linux and Vulkan. You can play games in a Chromium browser on a Linux desktop. It'`,
//             'publisher_name': `GamingOnLinux`,
//         },
//     ]
// }


let listArticles = {
    listArticles: [],
    header: '',

    init: function(articles) {
        this.listArticles = articles['list'];
        this.header = articles['header'];
    },

    render: function() {
        main = `
        <div class="top-headerbar">
        </div>
        <div id="header" class="header">
            <h1>${this.header}</h1>
        </div>
        
        <div class="feed">
            <div class="list-articles">
        `;
        for (article of this.listArticles) {
            articleElement = `
            <article class="row">    
                <a class="thumb col-md-3">
                    <img src="${article['thumb']}" alt="">
                </a>
                <div class="content col-md-9">
                    <a class="content-title" href="#" target="_blank">${article['title']}</a>
                    <button class="save-for-later" title="Read Later" type="button"></button>
                    <div class="content-metadata">
                        <span class="">
                            <a class="#">${article['publisher']['name']}</a>
                        </span>
                    </div>
                    <div class="content-sapo">${article['sapo']}</div>
                </div>
            </article>
            `,
            main += articleElement;
        }
        main += `
            </div>
        </div>
        `,
        document.getElementsByTagName('main')[0].innerHTML = main;

    }
}