document.getElementById('predictBtn').addEventListener('click', function(){
    const got_form = new FormData(document.getElementById('flagForm'));

    const values = {};
    got_form.forEach((value, key) => {
        if(value===''){
            values[key]=0
        }else{
            if (key.endsWith('s')) {
               values[key] = parseInt(value);
         } else if (value === "1"){
            values[key]= 1
         }else
            values[key]=0
        }   
    });
    console.log(values);
})