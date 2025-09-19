    
    function fromByte2Giga(v,n=2) {
        return (v / 1024  / 1024 /1024) ;
    }



    //Get a value with unit GigaBytes
    function getValue(elementID) {
            return fromByte2Giga( document.getElementById(elementID).textContent);
    }

    //Get a scalar value without a unit
    function getValueScalar(elementID) {
            return parseFloat(document.getElementById(elementID).textContent);
    }

    
