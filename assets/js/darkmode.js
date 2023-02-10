// theme switch example for demo

const toggleDarkMode = document.getElementById('btnSwitch')

toggleDarkMode.addEventListener('click',()=>{
  if (document.documentElement.classList.contains('dark')) {
      document.documentElement.classList.remove('dark')
      localStorage.setItem("theme", "light")
  }
  else {
      document.documentElement.classList.add('dark')
      localStorage.setItem("theme", "dark")
  }
})

const setDarkMode = (active = false) => {
    const wrapper = document.documentElement.classList;
    if (active) {
      wrapper.add('dark');
      toggleDarkMode.checked = true;
    } else {
      wrapper.remove('dark');
      toggleDarkMode.checked = false;
      localStorage.setItem("theme", "light");
    }
};

  // Query user preference and see if theme preference has been set
    const query = window.matchMedia("(prefers-color-scheme: dark)");
    const themePreference = localStorage.getItem("theme");

    let active = query.matches;

    if (themePreference === "dark") {
    active = true;
    }

    if (themePreference === "light") {
    active = false;
    }

    // Set theme based on user preference or override
    setDarkMode(active);

    // Watch for user preference changes
    query.addEventListener("change", (e) => setDarkMode(e.matches));
