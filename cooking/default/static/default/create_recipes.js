let ingredients_id=2;
let directions_id=2;
var on=false;

document.addEventListener('DOMContentLoaded', function() {
    document.querySelector('#add_ingredients').addEventListener('click', () => add_ingredients_function());
    document.querySelector('#add_directions').addEventListener('click', () => add_directions_function());
    document.querySelector('#save_button').addEventListener('click',()=> grab_information());
});

var loadFile = function(event) {
	var image = document.getElementById('output');
	image.src = URL.createObjectURL(event.target.files[0]);
};

function grab_information(){
    
    table=document.getElementById('ingredients_table').getElementsByTagName('tbody')[0].getElementsByTagName('input');
    // console.log(table);
    var ingr=[];var measurements=[];var directions=[];
    // console.log(table);
    for(var i=0;i<table.length;i++){
        if(i%2==0){
            //ingr
            ingr.push(table[i].value);
        }
        else{
            measurements.push(table[i].value);
        }
    }
    table=document.getElementById('directions_table').getElementsByTagName('tbody')[0].getElementsByTagName('textarea');
    for(var i=0;i<table.length;i++){
        directions.push(table[i].value);
    }
    console.log(ingr+" "+measurements+ " "+directions);
    document.getElementById('ingredients_list_hidden').setAttribute('value', ingr);
    document.getElementById('ingredients_measurements_hidden').setAttribute('value', measurements);
    document.getElementById('directions_hidden').setAttribute('value', directions);
    
    

    // document.getElementById('post_button').click();
}

function check_remove(index,headerRow,original_id){
    if(on){
        index.innerHTML=`<button type="button" id="closing_button"> Remove </button>`;
    }
    else{
        index.innerHTML=original_id;
    }
    if(document.getElementById('closing_button') != null){
        document.getElementById('closing_button').addEventListener('click', function(){
            remove_ingredient(headerRow,original_id);
        });
    }
}


function remove_ingredient(headerRow,original_id){
    var table_body=document.getElementById("ingredients_table").getElementsByTagName('tbody')[0];
    table_body.removeChild(headerRow);
    


        var inc = original_id-2,
        max = table_body.rows.length;
        delay = 200; 
        
        
    function timeoutLoop() {
        table_rows=table_body.getElementsByTagName('tr')[inc];
        
        table_rows.querySelector('td').innerHTML=`${inc+1}`; 
        table_rows.querySelector('td').setAttribute('id', `id${inc+1}`);

        // console.log(table_rows.querySelector('td').innerHTML +" "+ table_rows.querySelector('td').id);
        // console.log(inc+" "+max);

        if (++inc < max){
            setTimeout(timeoutLoop,delay);
        }
    }

    setTimeout(timeoutLoop, delay);

    
    ingredients_id=table_body.rows.length+1;
    
    
}

function add_ingredients_function(){
    var table_body=document.getElementById("ingredients_table").getElementsByTagName('tbody')[0];
    let headerRow = document.createElement("tr");
    headerRow.setAttribute('id', `${ingredients_id}`);

    let index = document.createElement("td");
    index.setAttribute('id', `id${ingredients_id}`);
    index.setAttribute('class', "ingredient_name_placeholder")
    index.innerHTML=`${ingredients_id}`;

    let headerCell1 = document.createElement("td");
    headerCell1.innerHTML=`<input type="text" placeholder="Ingredient_Name">`;

    let headerCell2 = document.createElement("td");
    headerCell2.innerHTML=`<input type="text" placeholder="measurement">`;

    headerRow.appendChild(index);
    headerRow.appendChild(headerCell1);
    headerRow.appendChild(headerCell2);

    table_body.appendChild(headerRow);

    const temp_id=ingredients_id;
    index.addEventListener('mouseenter', function(){
        on=true;
        check_remove(index,headerRow, temp_id);
    });
    index.addEventListener('mouseleave', function(){
        on=false;
        check_remove(index,headerRow, temp_id);
    });

    ingredients_id++;
}






//directions

//have to change the original_id


function check_remove_directions(index,headerRow){
    if(on){
        index.innerHTML=`<button type="button" id="closing_button"> Remove </button>`;
        // console.log("A");
    }
    else{
        index.innerHTML=`${headerRow.id}`;
        // console.log("A");
    }
    if(document.getElementById('closing_button') != null){
        document.getElementById('closing_button').addEventListener('click', function(){
            remove_direction(headerRow); 

            //if removed->then all objects after that id has to decrease its original id by 1

        });
    }
}


function remove_direction(headerRow){
    var table_body=document.getElementById("directions_table").getElementsByTagName('tbody')[0];
    var original_id=headerRow.id;
    table_body.removeChild(headerRow);
    

    
        var inc = original_id-1;
        var max = table_body.rows.length;
        delay = 200; 
        
    //    console.log(table_body);
    function timeoutLoop() {
        table_rows=table_body.getElementsByTagName('tr')[inc];
        if(inc>0 && inc<max){
        // console.log(inc+" "+max);
        // console.log(table_rows);
        // console.log(inc+" "+max);
        
        var tempindex=table_rows.querySelector(`#directions_number${inc+2}`);
        tempindex.setAttribute('id',`directions_number${inc+1}`);
        tempindex.innerHTML=inc+1;
        
        var temptext=table_rows.querySelector(`#directions_td${inc+2}`);
        temptext.setAttribute('id', `directions_td${inc+1}`);

        var temp_textarea=temptext.querySelector(`#directions_text${inc+2}`);
        temp_textarea.setAttribute('placeholder', `Direction ${inc+1}:`)
        temp_textarea.setAttribute('id',`directions_text${inc+1}` )
        
        table_rows.setAttribute('id', `${inc+1}`);
        }
        if (inc < max){
            setTimeout(timeoutLoop,delay);
            inc++;
        }
    }

    setTimeout(timeoutLoop, delay);

    
    directions_id=table_body.rows.length+1;
    
    
}





function add_directions_function(){
    var table_body=document.getElementById("directions_table").getElementsByTagName('tbody')[0];
    let headerRow = document.createElement("tr");
    headerRow.setAttribute('id', `${directions_id}`);


    let index = document.createElement("td");
    index.setAttribute('id', `directions_number${directions_id}`);
    index.setAttribute('class', `directions_number_placeholder`);
    
    index.innerHTML=`${directions_id}`;
    

    let textarea = document.createElement("td");
    textarea.setAttribute('id',`directions_td${directions_id}`);
    textarea.setAttribute('class', `directions_text_placeholder`);
    textarea.innerHTML=`<textarea class="form-control" id="directions_text${directions_id}" rows="2" placeholder="Direction ${directions_id}:"></textarea>`;
    
    headerRow.appendChild(index);
    headerRow.appendChild(textarea);

    table_body.appendChild(headerRow);

    index.addEventListener('mouseenter', function(){
        on=true;
        check_remove_directions(index,headerRow);
    });
    index.addEventListener('mouseleave', function(){
        on=false;
        check_remove_directions(index,headerRow);
    });

    directions_id++;


}