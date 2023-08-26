const text = document.querySelector('#submitted');
const endTexts = ["Your <span class='makered'>destiny</span> lies in the hands of the prophecy.", "The uncertainty of <span class='makered'>future</span> lies in the past.", "With the hidden answers, your <span class='makered'>fate</span> stays hidden.", "In an ever shifting maze of <span class='makered'>possibilites</span>,<br>This one may or may not be in your favour."];
const index = Math.floor(Math.random() * endTexts.length);
text.innerHTML = endTexts[index];

text.style.display = "none";

setTimeout(displayText, 4000);

function displayText(){
    text.style.display = "block";
}