async function getAPI(){
    const API_URL = 'https://reqres.in/api/users'
    let x = await fetch(API_URL)
    .then(res => res.json())
    .then(data => console.log(data))
}

getAPI()