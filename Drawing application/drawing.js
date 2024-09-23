let studentslist =[]
const ul = document.querySelector("ul");
const nstudents = document.querySelector("#nstudents");
const adding = document.querySelector("form");
const reset = document.querySelector("#reset");
const rand = document.querySelector("#rand");
const p = document.createElement("p");
reset.after(p)
//-----------------------------------------------------------------------------
adding.addEventListener("submit", function (e){
    e.preventDefault();
    const name = document.querySelector("#name");
    const lname = document.querySelector("#lname");
    const err = document.querySelector("#err");
    const allname = name.value.concat(" ",lname.value);
    if (name.value.length === 0 || lname.value.length === 0){
        err.textContent="Please fill all the fields";
    }
    else {
        if (studentslist.some(student => student.name === allname)){
            err.textContent = "Student " + allname +" has been already added";
        }
        else {
            studentslist.push({name:allname, selected:false});
            err.textContent = "";
            const li = document.createElement("li");
            studentslist.forEach((student) => {
                li.textContent = student.name;
                ul.appendChild(li)
            })
        nstudents.textContent = "["+ studentslist.length+"]";
        }


        name.value = "";
        lname.value = "";


    }
})
//-----------------------------------------------------------------------------
reset.addEventListener("click", function (e){
    e.preventDefault()
    const con = confirm("Are you sure you want to reset?")
    if (con){
        studentslist =[]
        ul.innerHTML = "";
        nstudents.textContent = "";
    }


})

rand.addEventListener("click", function (e){
    e.preventDefault()
    

    if (studentslist.length>0){
        if (studentslist.every(student => student.selected)) {
            p.textContent = "All students have been drawn";
        } else {
            let num =Math.floor(Math.random() * studentslist.length)
            while (studentslist[num].selected){
                num = Math.floor(Math.random() * studentslist.length)
            }
            studentslist[num].selected = true
            p.textContent = "calling " + studentslist[num].name;
            }
        }
    else {
        p.textContent = "Add students to the list before drawing"
    }


})