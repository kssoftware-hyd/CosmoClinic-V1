(function(){var m=document.getElementById('hx-modal');if(!m)return;var last;
function $(i){return document.getElementById(i)}function err(i,s){$('hx-e-'+i).textContent=s||'';return !s}
function open(){last=document.activeElement;m.classList.add('open');m.setAttribute('aria-hidden','false');$('hx-name').focus()}
function close(){m.classList.remove('open');m.setAttribute('aria-hidden','true');try{sessionStorage.setItem('hxo','1')}catch(e){}if(last&&last.focus)last.focus()}
document.querySelectorAll('[data-open-offer]').forEach(function(x){x.addEventListener('click',function(e){e.preventDefault();open()})});
$('hx-close').addEventListener('click',close);m.addEventListener('click',function(e){if(e.target===m)close()});document.addEventListener('keydown',function(e){if(e.key==='Escape'&&m.classList.contains('open'))close()});
var seen=false;try{seen=sessionStorage.getItem('hxo')}catch(e){}if(!seen)setTimeout(function(){if(!m.classList.contains('open'))open()},8000);
$('hx-offer-form').addEventListener('submit',function(e){e.preventDefault();var p=$('hx-phone').value.replace(/[\s-]/g,''),ok=true;
ok=err('name',$('hx-name').value.trim().length<2?'Please enter your name.':'')&&ok;ok=err('phone',/^(\+?91)?[6-9]\d{9}$/.test(p)?'':'Enter a valid 10-digit mobile number.')&&ok;
ok=err('treat',$('hx-treat').value?'':'Please choose a treatment.')&&ok;ok=err('consent',$('hx-consent').checked?'':'Please tick to agree.')&&ok;if(!ok)return;
var t='Hello Cosmo International Clinic, I would like to claim the offer.\nName: '+$('hx-name').value.trim()+'\nPhone: '+p+'\nTreatment: '+$('hx-treat').value;
window.open('https://wa.me/919246119111?text='+encodeURIComponent(t),'_blank','noopener');close()});
var cs=document.querySelectorAll('[data-count]'),done=false;function run(){if(done)return;done=true;cs.forEach(function(el){var to=+el.dataset.count,s=null;function st(ts){s=s||ts;var k=Math.min((ts-s)/1200,1);el.textContent=Math.round(to*k);if(k<1)requestAnimationFrame(st)}requestAnimationFrame(st)})}
if('IntersectionObserver' in window&&cs.length){new IntersectionObserver(function(en,o){if(en[0].isIntersecting){run();o.disconnect()}}).observe(cs[0])}else run()})();
