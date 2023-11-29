const contentContainer = document.getElementById('content-container')
const loginForm = document.getElementById('login-form')
const searchForm = document.getElementById('search-form')

const baseEndpoint = "http://localhost:8000/api"

if (loginForm){
    loginForm.addEventListener('submit', handleLogin)
}

if (searchForm){
    searchForm.addEventListener('submit', handleSearch)
}

function handleLogin(event){
    // prevent the browser from submitting the form in the default way, and instead use the custom function to handle the login process.
    event.preventDefault();
    const loginEndpoint = `${baseEndpoint}/token/`

    // The FormData class is a class that provides an easy way to construct a set of key-value pairs that represent form fields and their values.
    let loginFormData = new FormData(loginForm )

    // The Object.fromEntries function is a function that creates a new object from an iterable of key-value pairs, such as an array or a map. 
    let loginObjectData = Object.fromEntries(loginFormData)

    // The JSON.stringify function is a function that converts a JavaScript value to a JSON string. 
    let bodyStr = JSON.stringify(loginObjectData)
    // console.log(loginObjectData, bodyStr)
    const options = {
        method : "POST",
        headers : {
            "Content-Type": "application/json"
        },
        body : bodyStr
    }
    fetch(loginEndpoint, options)
    .then(response =>{
        // console.log(response)
        return response.json()
    })
    .then(authData =>{
        handleAuthData(authData, getProductList)
    })
    .catch(err =>{
        console.log("ERROR ", err)
    })
}


function handleSearch(event){
    event.preventDefault();

    let formData = new FormData(searchForm)
    let data = Object.fromEntries(formData)
    let searchParams = new URLSearchParams(data)

    const endpoint = `${baseEndpoint}/search/?${searchParams}`
    // const headers = {
    //     "Content-Type" : "application/json",
    // }

    // const authToken = localStorage.getItem('access')
    // if (authToken){
    //     headers['Authorization'] = `Bearer ${authToken}`
    // }
    
    // const options = {
        //     method : "GET",
        //     headers : headers
        // }

    const options = getFetchOptins()
    fetch(endpoint, options)
    .then(response =>{
        return response.json()
    })
    .then(data =>{
        // console.log(data.hits)
        writeToContainer(data)
    })
    .catch(err =>{
        console.log("ERROR ", err)
    })
}




function handleAuthData(authData, callback){
    localStorage.setItem('access', authData.access)
    localStorage.setItem('refresh', authData.refresh)
    if (callback){
        callback()
    }
}


function writeToContainer(data){
    if (contentContainer){
        contentContainer.innerHTML = "<pre>" + JSON.stringify(data, null, 4) + "</pre>"
    }
}

function getFetchOptins(method, body){
    return {
        method : method === null ? "GET" : method,
        headers : {
            "Content-Type": "application/json",
            "Authorization":`Bearer ${localStorage.getItem('access')}` 
        }, 
        body : body ? body : null
    }
}



function isTokenNotValid(jsonData){
    if (jsonData.code && jsonData.code === "token_not_valid"){
        alert("Please login again!")
        return false
    }
    return true
}


function validateJWTToken(){
    const endpoint = `${baseEndpoint}/token/verify/`
    const options = {
        method : "POST",
        headers : {
            "Content-Type" : "application/json"
        },
        body : JSON.stringify({
            token : localStorage.getItem('access')
        })
    }
    fetch(endpoint, options)
    .then(response => response.json())
    .then(x =>{
        // refresh token
    })
}


function getProductList(){
    const endpoint = `${baseEndpoint}/products/`
    const options = getFetchOptins()
    fetch(endpoint, options)
    .then(response => {
        // console.log(response)
        return response.json()
    })
    .then(data =>{
        // console.log(data)
        const validData = isTokenNotValid(data)
        if (validData){
            writeToContainer(data)
        }
    })
}

validateJWTToken()

