$(document).ready(function(){
    $('.icon').click(function(){
        $('.search').toggleClass('active');
    });
});
 

var RandomColorTags = ()=>{
    TagsColor = ['badge success','badge danger','badge info','badge primary','badge warning' ]
    tagsLink = document.getElementsByClassName('tag')
     
     
    
    Array.from(tagsLink).forEach((link) => {
        link.setAttribute("class", TagsColor[Math.floor(Math.random() * TagsColor.length)]);
    });
}


RandomColorTags()


 
