document.addEventListener("DOMContentLoaded", () => {
    const word = document.getElementById('word')
    const synm = document.getElementById('syn')
    synm.addEventListener('click',async(event)=>{
        const res = await fetch(`/api/getSynm/${word.value}`)
        console.log(res)
        const words = await res.json()
        addNewWords(words)
    })
})


function addNewWords(words) {
    const cont = document.getElementsByTagName('tbody')[0]
    const elements = document.getElementsByTagName('tr')
    if (elements.length > 0) {
        for(let el of elements) {
            el.remove()
        }
        for(let a of words) {
            let tr = document.createElement('tr')
            tr.innerHTML = `<td>${a}</td> `
            cont.appendChild(tr)
        }
    }
    else {
        for(let a of words) {
            let tr = document.createElement('tr')
            tr.innerHTML = `<td>${a}</td> `
            cont.appendChild(tr)
        }
    }
}