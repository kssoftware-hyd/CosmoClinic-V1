/* extras.js - finds the right file extension for images marked data-auto
   (jpg / jpeg / png / webp, lower or UPPER case) and hides optional images that do not exist. */
(function(){
  'use strict';
  var EXT=['jpg','jpeg','png','webp'];
  function cands(img){
    var src=img.getAttribute('data-src0')||img.getAttribute('src');
    img.setAttribute('data-src0',src);
    var base=src.replace(/\.(jpe?g|png|webp)$/i,'');
    var slash=base.lastIndexOf('/')+1,dir=base.slice(0,slash),name=base.slice(slash);
    var names=[name];
    if(name.toUpperCase()!==name)names.push(name.toUpperCase());
    var out=[];
    names.forEach(function(n){EXT.forEach(function(e){
      [e,e.toUpperCase()].forEach(function(x){var s=dir+n+'.'+x;if(s!==src&&out.indexOf(s)<0)out.push(s);});
    });});
    return out;
  }
  function fail(img){
    var list=img._c||(img._c=cands(img)),i=img._i||0;
    if(i<list.length){img._i=i+1;img.src=list[i];return;}
    var w=img.closest('figure,.hx-ph');(w||img).classList.add('img-missing');
  }
  function ok(img){
    var b=img.closest('button.plain');
    if(b)b.setAttribute('data-img',img.getAttribute('src'));
  }
  function init(){
    var imgs=document.querySelectorAll('img[data-auto]');
    for(var k=0;k<imgs.length;k++){(function(img){
      img.addEventListener('error',function(){fail(img);});
      img.addEventListener('load',function(){ok(img);});
      if(img.complete){if(img.naturalWidth===0&&img.getAttribute('src'))fail(img);else ok(img);}
    })(imgs[k]);}
  }
  if(document.readyState==='loading')document.addEventListener('DOMContentLoaded',init);else init();
})();
