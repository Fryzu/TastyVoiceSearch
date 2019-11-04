function renderList(jsonData) {
  print(jsonData);

  var listDiv1 = document.getElementById("recipes-list1");
  var listDiv2 = document.getElementById("recipes-list2");

  for (var i = 0; i < 9; ++i) {
    // CardBody content
    var title = document.createElement("h5");
    title.setAttribute("class", "card-title");
    title.innerHTML = "Title";

    var text = document.createElement("p");
    text.setAttribute("class", "card-text");
    text.innerHTML = "text";

    var link = document.createElement("a");
    link.setAttribute("class", "btn btn-primary");
    link.setAttribute("href", "#");
    link.innerHTML = "Check out";

    // Card content
    var image = document.createElement("img");
    image.setAttribute("class", "card-img-top");
    image.setAttribute(
      "src",
      "https://www.thesprucepets.com/thmb/daHAnhowPummm2Uqe1O5drHsp-8=/960x0/filters:no_upscale():max_bytes(150000):strip_icc():format(webp)/golden-retriever-sitting-down-in-a-farm-837898820-5c7854ff46e0fb00011bf29a.jpg"
    );

    var cardBody = document.createElement("div");
    cardBody.setAttribute("class", "card-body");
    cardBody.appendChild(title);
    cardBody.appendChild(text);
    cardBody.appendChild(link);

    // Card
    var card = document.createElement("div");
    card.setAttribute("class", "card m-3");
    card.setAttribute("style", "");
    card.appendChild(image);
    card.appendChild(cardBody);

    if (i % 2 === 1) {
      listDiv2.appendChild(card);
    } else {
      listDiv1.appendChild(card);
    }
  }
}

$.getJSON("http:localhost:8080", function(data) {
  console.log(data);
});
