const btnWeather = document.querySelector('#btnWeather');
const txtCity = document.querySelector('#txtCity');
const resultOut = document.querySelector('#result');
let cityList = [];

fetch("city.list.json").then( response => {
    response.json().then( data => {
        cityList = data;
    });

}).catch(err => console.log (err.message));


btnWeather.onclick = function() {
  if (cityList.length === 0) { resultOut.innerHTML = "CityList did not load."; }
  let output = "";
//   const city = txtCity.value;
//   const url = `http://api.openweathermap.org/data/2.5/weather?q=${city}&appid=${KEY}`;
//   fetch(url).then(response => {
//     response.json().then(json => {
//       let data = json;
//       let output = formatResponse(data);
//       resultOut.innerHTML = output;
//     })
//   });
    const cityInfo = getCityID(txtCity.value);
    if (cityInfo.length > 0) {
        let cityID = "";
        let cityCty = "";
        let cityLat = "";
        let cityLon = "";
        // Find US first. Post first US then suggest other options.
    
    
        // post first city info
        cityID = cityInfo[0].id;
        cityCty = cityInfo[0].country;
        cityLat = cityInfo[0].coord.lat;
        cityLon = cityInfo[0].coord.lon;
        // console.log(`CityID: ${cityID}, Country: ${cityCty}, Coord: Lat ${cityLat}, Long ${cityLon}. All Data available.`);
        const url = `http://api.openweathermap.org/data/2.5/weather?id=${cityID}&appid=${KEY}`;
        // console.log(url);
        fetch(url).then( response => {
            response.json().then(json => {
                let data = json;
                let output = formatResponse(data);
                resultOut.innerHTML = output;
            });
        });
    } else {
        // Tell them something went wrong;
        resultOut.innerHTML = "<p><strong>City information not found.</strong> Please check your spelling and try again.</p>";
    }
    
}

function getCityID(txtCity) {
    return cityList.filter(
        item => item.name === txtCity
    );
}

function kelvinToFahrenheit(ktemp) {
    let ftemp = ktemp * (9/5) - 459.67;
    return ftemp;
}

function kelvinToCelsius(ktemp) {
    let ctemp = ktemp - 273.15;
    return ctemp;
}

function msToMPH(ms) {
    return (ms*2.237);
}

function msToKPH(ms) {
    return (ms*3.6);
}


function formatResponse(data) {
    let conditions  = "";
    // let icons = "";
    if(data.weather.length>1) {
        for(var i = 0; i < data.weather.length; i++) {
            conditions += data.weather[i].description;
            icons += `<img src="http://openweathermap.org/img/wn/${data.weather[i].icon}@2x.png" />`;
            if (i != data.weather.length-1) {
                conditions += " and ";
            }
        }
    } else {
        conditions = data.weather[0].description;
        icons = `<img src="http://openweathermap.org/img/wn/${data.weather[0].icon}@2x.png" />`;
    }
    let out = `<p><strong>Current conditions for ${data.name} in ${data.sys.country}</strong></p>
    <p><strong>Tempurature:</strong> ${Math.round(kelvinToFahrenheit(data.main.temp))}&deg; F / ${Math.round(kelvinToCelsius(data.main.temp))}&deg; C</p>
    <p><strong>Humidity:</strong> ${data.main.humidity}%</p>
    <p><strong>Pressure:</strong> ${data.main.pressure}mb</p>
    <p><strong>Wind:</strong> ${data.wind.deg} degrees at ${msToMPH(Math.round(data.wind.speed))} MPH (${msToKPH(Math.round(data.wind.speed))} KPH)</p>
    <p class="description">${conditions} ${icons}</p>`;
    return out;
}