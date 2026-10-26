(function(){var f=document.getElementById('enquiry');if(!f)return;
function $(i){return document.getElementById(i)}function err(i,m){$('e-'+i).textContent=m||'';return !m}
f.addEventListener('submit',function(e){e.preventDefault();var ok=true,p=$('phone').value.replace(/[\s-]/g,'');
ok=err('name',$('name').value.trim().length<2?'Please enter your name.':'')&&ok;
ok=err('phone',/^(\+?91)?[6-9]\d{9}$/.test(p)?'':'Enter a valid 10-digit mobile number.')&&ok;
ok=err('email',!$('email').value||/^[^@\s]+@[^@\s]+\.[^@\s]+$/.test($('email').value)?'':'Enter a valid email.')&&ok;
ok=err('treatment',$('treatment').value?'':'Please choose a treatment.')&&ok;
ok=err('date',!$('date').value||$('date').value>=new Date().toISOString().slice(0,10)?'':'Choose a future date.')&&ok;
ok=err('message','')&&ok;ok=err('consent',$('consent').checked?'':'Please tick to agree.')&&ok;if(!ok)return;
var t='Hello Cosmo International Clinic,\nName: '+$('name').value.trim()+'\nPhone: '+p+($('email').value?'\nEmail: '+$('email').value:'')+'\nTreatment: '+$('treatment').value+($('date').value?'\nPreferred date: '+$('date').value:'')+($('message').value.trim()?'\nMessage: '+$('message').value.trim():'');
window.open('https://wa.me/919246119111?text='+encodeURIComponent(t),'_blank','noopener')})})();
