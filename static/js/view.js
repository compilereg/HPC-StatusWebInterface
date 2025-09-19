function printControlInfo() {
        
        //Get the host state
        Response=getJsonFromUrl(API_URL+"/get/hoststate/"+CONTROLIP)
        .then(data => {
            if (data) {               
               document.getElementById('ctrl_state').innerHTML="<img src='images/working.png' width=30% height=30%>Live";
                // You can now work with the 'data' object
            } else {
               
               document.getElementById('ctrl_state').innerHTML="<img src='images/notworking.png' width=30% height=30%>Dead";
               return;
            }
        });

        
        //Get the host mame
        Response=getJsonFromUrl(API_URL+"/get/hostname/"+CONTROLIP)
        .then(data => {
            if (data) {
                document.getElementById('ctrl_hostname').textContent = data['data'];
                // You can now work with the 'data' object
            } else {
                console.log("Failed to retrieve JSON data.");
            }
        });
      
        
        //Get the host memory
        Response=getJsonFromUrl(API_URL+"/get/hostmem/"+CONTROLIP)
        .then(data => {
            if (data) {
                
                document.getElementById('ctrl_mem_total').textContent = fromByte2Giga(data['Memory']['Total']).toFixed(2);
                document.getElementById('ctrl_mem_used').textContent = fromByte2Giga(data['Memory']['Used']).toFixed(2);
                document.getElementById('ctrl_mem_free').textContent = fromByte2Giga(data['Memory']['Free']).toFixed(2);

                        
                        google.charts.setOnLoadCallback(drawChartMemory);


                document.getElementById('ctrl_swap_total').textContent = fromByte2Giga(data['Swap']['Total']).toFixed(2);
                document.getElementById('ctrl_swap_used').textContent = fromByte2Giga(data['Swap']['Used']).toFixed(2);
                document.getElementById('ctrl_swap_free').textContent = fromByte2Giga(data['Swap']['Free']).toFixed(2);

                        google.charts.setOnLoadCallback(drawChartSwap);
                // You can now work with the 'data' object
            } else {
                console.log("Failed to retrieve JSON data.");
            }
        });

        //Get the host load average
        Response=getJsonFromUrl(API_URL+"/get/hostavgload/"+CONTROLIP)
        .then(data => {
            if (data) {                
                document.getElementById('ctrl_loadavg_1m').textContent = data['AvgLoad']['1Min'];
                document.getElementById('ctrl_loadavg_5m').textContent = data['AvgLoad']['5Min'];
                document.getElementById('ctrl_loadavg_15m').textContent = data['AvgLoad']['15Min'];
                if (data['AvgLoad']['1Min'] > data['AvgLoad']['5Min'] && data['AvgLoad']['5Min'] >  data['AvgLoad']['15Min']) { //Increase load
                    document.getElementById('ctrl_loadavg_state').innerHTML = '\&uarr;'; 
                }
                else {
                    document.getElementById('ctrl_loadavg_state').innerHTML = '\&darr;';    
                }
                google.charts.setOnLoadCallback(drawChartLoadAVG);
                // You can now work with the 'data' object
            } else {
                console.log("Failed to retrieve JSON data.");
            }
        });      
    }
