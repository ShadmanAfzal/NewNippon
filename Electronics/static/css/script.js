function hide() {
    console.log("hello");
    var abc = document.getElementById("info");
      if(abc.style.display == "none")
      {
          abc.style.display = "block";
      }
      else{
          abc.style.display = "none";
      }
    }

