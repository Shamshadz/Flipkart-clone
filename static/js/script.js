const header = document.querySelector('.Header');
const nav = document.querySelector('.Navbar')
const topOfNav = header.offsetTop;

function fixNav(){
    if (window.scrollY >= topOfNav){
        nav.style.paddingTop = header.offsetHeight + 2 + 'px';
    }
    else{
        nav.style.paddingTop = 0;
    }
}
// for fixing the navbar at top
window.addEventListener('scroll',fixNav);


// function showItemFunc(){
//     var element = document.querySelector('.showItem');
//     element.innerHTML = element.innerText || element.textContent;
//     console.log(element.innerHTML)
// }



// $(function (){ 
//     $('.addBtn').on('click', function(){ 
//         //Fetch Id 
//         var id = $(this).data('id');
        
        
//         $ajax({
//             type: "POST",
//             url: '/cart',   
//             data: {csrfmiddlewaretoken: '{{ csrf_token }}',
//                   id : id},   /* Passing the text data */
//             success:  function(response){
//                    alert(response);
//                }
//         });


// //         var element = document.getElementById(`${id}`)
// //         element.innerHTML = element.innerText || element.textContent;
// //         console.log(element.innerHTML)
        
//     }); 
// }); 