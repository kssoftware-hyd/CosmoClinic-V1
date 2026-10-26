(function(){var b=document.getElementById('burger'),n=document.getElementById('nav');
if(b&&n)b.addEventListener('click',function(){var o=n.classList.toggle('open');b.setAttribute('aria-expanded',o)});
document.querySelectorAll('.ddbtn').forEach(function(x){x.addEventListener('click',function(e){e.stopPropagation();var d=x.parentNode,o=d.classList.toggle('open');x.setAttribute('aria-expanded',o)})});
document.addEventListener('click',function(){document.querySelectorAll('.dd.open').forEach(function(d){d.classList.remove('open')})});
var lb=document.getElementById('lb'),im=document.getElementById('lbimg'),cp=document.getElementById('lbcap');
function close(){if(lb)lb.hidden=true}
document.querySelectorAll('[data-img]').forEach(function(x){x.addEventListener('click',function(){im.src=x.dataset.img;im.alt=x.dataset.cap||'';cp.textContent=x.dataset.cap||'';lb.hidden=false})});
var c=document.getElementById('lbclose');if(c)c.addEventListener('click',close);if(lb)lb.addEventListener('click',function(e){if(e.target===lb)close()});
document.addEventListener('keydown',function(e){if(e.key==='Escape'){close();if(n)n.classList.remove('open')}})})();
