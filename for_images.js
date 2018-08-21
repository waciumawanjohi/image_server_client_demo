function fetch_image(img_address){
    fetch(img_address).then(function(response){
        if (response.ok){
            response.blob().then(function(blob){
                var image_URL = URL.createObjectURL(blob);
                var image = document.getElementById("place_image");
                image.src = image_URL;
            });
        } else {
            alert(response.statusText);
        }
    });
}

fetch_image("http://localhost:5000/get_image/2");
