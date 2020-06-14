document.addEventListener("DOMContentLoaded", () => {
    var page_num = 1;
    const getNews = document.getElementById('more')
  



    getNews.addEventListener('click',async(event)=>{
        page_num++
        const res = await fetch(`/api/getNews/${page_num}`)
        console.log(res)
        const news = await res.json()
        addNewNews(JSON.parse(news))
    })


})

function addNewNews (news){
    const tableNews = document.getElementsByTagName('tbody')[0]
    const rowIndex = document.getElementsByClassName('rows')
    let rowCount = Number(rowIndex[rowIndex.length -1].innerText)
    for(let a of news){
        rowCount++
        let tr = document.createElement('tr')
        tr.innerHTML = `<th scope="row" class='rows'>${rowCount}</th>  <td><a href="news/${a._id}"> ${a.newsName}</a> </td> <td>${a.newsDate}</td>`
        tableNews.appendChild(tr)
    }

}