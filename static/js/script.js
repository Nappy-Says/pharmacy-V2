let searchWrapper = document.querySelector('.search-input')
let inputBox = searchWrapper.querySelector('input')
let suggBox = searchWrapper.querySelector('.autocom-box')

inputBox.onkeyup = e => {
    let userData = e.target.value
    let emptyArray = []
    if(userData){
        emptyArray = suggestions.filter(data => 
            data
                .toLocaleLowerCase()
                .includes(userData.toLocaleLowerCase())
        )
        emptyArray = emptyArray.map(data => '<li>' + data + '</li>')
        searchWrapper.classList.add("active")
        showSuggestions(emptyArray)
        let allList = suggBox.querySelectorAll("li")
        for (let i = 0; i < allList.length; i++) {
            allList[i].setAttribute('onclick', 'select(this)')
        }
    }else{
        searchWrapper.classList.remove("active")
        suggBox.innerHTML = ""
    }
}

function select(element){
    let selectUserData = element.textContent
    inputBox.value = selectUserData
    searchWrapper.classList.remove("active")
    suggBox.innerHTML = ""
}

function inputClear(){
    inputBox.value = ""
    suggBox.innerHTML = ""
    searchWrapper.classList.remove("active")
}

function showSuggestions(list){
    let listData = list.join('')
    
    if(!list.length) 
        suggBox.innerHTML = "Empty"
    else{
        listData = list.join('')
        suggBox.innerHTML = listData
    }
    
}

$('.myDataTable').DataTable({
    searching: true
})