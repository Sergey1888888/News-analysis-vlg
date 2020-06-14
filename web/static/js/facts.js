document.addEventListener("DOMContentLoaded", () => {
    var page_num = 1;
    const getFacts = document.getElementById('moreFacts')


    getFacts.addEventListener('click',async(event)=>{
        page_num++
        const res = await fetch(`/api/getFacts/${page_num}`)
        console.log(res)
        const facts = await res.json()
        addNewFacts(JSON.parse(facts))
    })


})


function addNewFacts(facts){
    const tableNews = document.getElementsByTagName('tbody')[0]
    const rowIndex = document.getElementsByClassName('rows')
    let rowCount = Number(rowIndex[rowIndex.length -1].innerText)
    for(let a of facts){
        rowCount++
        let fact = ""
       
        for(let f of a.newsWithMention){
            fact += String(f) + '<br>'
        }
        console.log(fact)

        let tr = document.createElement('tr')
        tr.innerHTML = `<th scope="row" class='rows'>${rowCount}</th> <td>${fact}</td>  <td><a href="/news/${a._id}">Link</a> </td> `
        tableNews.appendChild(tr)
    }

}