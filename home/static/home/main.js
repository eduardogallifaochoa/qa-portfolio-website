let currentTheme = localStorage.getItem('theme');

if(currentTheme === 'dark-theme') {
    setTheme('dark-theme');
} else {
    setTheme('light-theme');
}

function setTheme(themeName) {
    localStorage.setItem('theme', themeName);
    document.documentElement.setAttribute("data-theme", themeName);
}

function switchTheme() {
    if(currentTheme === 'light-theme') {
        setTheme('dark-theme');
        currentTheme = 'dark-theme'
    } else if(currentTheme === 'dark-theme') {
        setTheme('light-theme');
        currentTheme = 'light-theme'
    }
}