function setCookie(cname, cvalue, exdays) {
    const d = new Date();
    d.setTime(d.getTime() + exdays * 24 * 60 * 60 * 1000);
    let expires = "expires=" + d.toUTCString();
    document.cookie =
        cname + "=" + cvalue + ";" + expires + ";path=/";
}

function getCookie(cname) {
    let name = cname + "=";
    let ca = document.cookie.split(";");
    for (let i = 0; i < ca.length; i++) {
        let c = ca[i];
        while (c.charAt(0) == " ") {
            c = c.substring(1);
        }
        if (c.indexOf(name) == 0) {
            return c.substring(name.length, c.length);
        }
    }
    return "";
}

function setDefaultTheme() {
    if (getCookie("theme") == "") {
        setCookie("theme", "dark", 1);
    }
}

function toggleTheme() {
    var theme = document.getElementsByTagName("link")[0];
    if (getCookie("theme") != "light" && getCookie("alertPop") != "true") {
        alert("Light theme is buggy (Neocities won't load the actual css file properly")
        setCookie("alertPop", "true", 1);
    }
    if (theme.getAttribute("href") == "style.css") {
        theme.setAttribute("href", "style_light.css");
        setCookie("theme", "light", 1);
    } else {
        theme.setAttribute("href", "style.css");
        setCookie("theme", "dark", 1);
    }
}

function themeChecker() {
    var theme = document.getElementsByTagName("link")[0];
    if (getCookie("theme") == "light") {
        theme.setAttribute("href", "style_light.css");
    }
}
