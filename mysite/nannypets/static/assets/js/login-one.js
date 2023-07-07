const button = document.querySelector("#cadastrar")
const modal = document.querySelector("dialog")
const page = document.querySelector(".page-full")
const buttonClose = document.querySelector(".but-esc")


button.onclick = function() {
    modal.showModal()
    modal.style.display = "flex"
    page.style.filter= "grayscale(45%)"
    page.style.opacity= "80%"
    document.onkeydown = function(e) {
        if(e.key === 'Escape') {
            modal.style.display = "none"
            page.style.filter= "grayscale(0%)"
            page.style.opacity= "100%"
        }
      }
}

buttonClose.onclick = function() {
    modal.close()
    modal.style.display = "none"
    page.style.filter= "grayscale(0%)"
    page.style.opacity= "100%"
}

