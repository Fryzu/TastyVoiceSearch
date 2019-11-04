function renderList(jsonData) {
  console.log(jsonData[0]);

  var listDiv1 = document.getElementById("recipes-list1");
  var listDiv2 = document.getElementById("recipes-list2");

  for (var i = 0; i < jsonData.length; ++i) {
    recipe = jsonData[i];

    // CardBody content
    var title = document.createElement("h5");
    title.setAttribute("class", "card-title");
    title.innerHTML = recipe.title;

    var text = document.createElement("p");
    text.setAttribute("class", "card-text");
    text.innerHTML = recipe.publisher;

    var link = document.createElement("a");
    link.setAttribute("class", "btn btn-primary");
    link.setAttribute("href", recipe.f2f_url);
    link.innerHTML = "Read more!";

    // Card content
    var image = document.createElement("img");
    image.setAttribute("class", "card-img-top");
    image.setAttribute("src", recipe.image_url);

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
  renderList(data);
});
