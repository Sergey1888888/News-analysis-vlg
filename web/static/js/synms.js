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


function addNewWords(words){
    const cont = document.getElementsByClassName('container')[1]
    let ul = document.createElement('ul')
    
    let li = ""
    for(let a of words){
        

        li += `<li>${a} </li>`
          
    }
    ul.innerHTML = li;
    cont.append('Введенное слово: '+word.value)
    cont.append(document.createElement('br'))
    cont.append('Синонимы: ')
    cont.appendChild(ul)

}