'use client';
import React, { useState } from "react";

const onButtonClick = async() => {
  console.log("Button clicked");

  const address = document.getElementById("address").value;
  const remainingMonths = document.getElementById("remainingMonths").value;
  const storeyLevel = document.getElementById("storeyLevel").value;

  try{
    var url = "http://127.0.0.1:5000"
    const response = await fetch(url, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({address: address, remainingMonths: remainingMonths, storeyLevel: storeyLevel})
    });
    
    const data = await response.json();
    console.log(data);

    const h1Element = document.getElementById("result");
    h1Element.textContent = JSON.stringify(data);
    

  }catch(error){
    console.error("Error: ", error);
  }
  
}


function Body(){
  return(
        <div>
          <div id="searchBar">
            <div className="w-4/5 mx-auto">
              <h1 className="flex items-center justify-center text-white font-bold text-3xl">
                Enter Address here
              </h1>
              <div className="flex justify-center p-2">
                <input className="searchInput pl-2" placeholder="Type address" id="address"/>
              </div>
              <div className="flex justify-center p-2">
                <input className="searchInput2 pl-2 mr-2" placeholder="Remaining months" id="remainingMonths"/>
                <input className="searchInput2 pl-2" placeholder="Storey level" id="storeyLevel"/>
              </div>
            </div>
          </div>

          <div className="flex justify-center">
            <button className="searchButton" onClick={onButtonClick}>Submit</button>
          </div>

          <div className="flex justify-center">
            <h1 id="result" className="text-white"></h1>
          </div>
        </div>

        
  )
}


export default Body;

