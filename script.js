const root = document.documentElement;
document.getElementById("theme").onclick = () => {
  const t = root.dataset.theme === "dark" ? "light" : "dark";
  root.dataset.theme = t;
  try { localStorage.setItem("theme", t); } catch (e) {}
};
document.getElementById("y").textContent = new Date().getFullYear();
