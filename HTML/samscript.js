var x = document.getElementById("demo");
var abc;
var availableTags = [
"Winberie's Restaurant & Bar","Milano Market","1020 Bar","Community Food & Juice","MIT Museum","Boston Tea Stop","Rack & Soul","Upstairs On the Square","Greek Corner Restaurant II","Society Coffee","EVOO","Beijing Tokyo","Otto Pizza","Boloco","Antonio's","Charlie's Kitchen","Cafe of India","Suma Sushi","Massachusetts Institute of Technology","Om Restaurant & Lounge","Tealuxe","The Cathedral Church of Saint John the Divine","Massawa","East Dumpling House","Lyndell's Bakery","SubsConscious","Maoz Vegetarian","Amherst Brewing Co","Sweet","Daedalus Restaurant & Pub","Think Tank","Hi-Rise At the Blacksmith House","Patisserie Des Ambassades","All Asia Bar","Melba's","Ferry House","Mill Korean","Rendezvous In Central Square","Sandrine's","Legal Sea Foods","Café 47","Chutney's","Bondir","Cambridge Bicycle","Green Street","Fruity Yogurt","Havana Central","Le's Restaurant","Cafe Pamplona","India Pavilion Restaurant","The Muddy Charles Pub at MIT","PARK Restaurant & Bar","Sugar+Sunshine Bakery","JP Licks","Shays Pub & Wine Bar","Tory Row","Kitchenette Uptown","Wondee Siam V","Salts Restaurant","Atkins Farms","Café Luna","Veggie Galaxy","Loews Harvard Square","Le Monde","Corner Tavern","Cafe Sushi","Blue Point Grill","Judie's","Lord Hobo","Artist & Craftsman Supply","Harvard Square","Small World Coffee","Mary Chung Restaurant","Mariposa Bakery","Mr. Bartley's Burger Cottage","Trata","Blockheads","Emma's Pizza","Brattle Square Florist","Max Soha","Shabu-Ya","Deluxe on Broadway","Crepes on Columbus","Fresh Side","Chipotle Mexican Grill","Newbury Comics","IHOP","Grendel's Den Restaurant & Bar","Qdoba","A Cafe New York","Herrell's Ice Cream","Harvest","Sakura Express","Crazy Dough's Pizza","Amsterdam Restaurant & Tapas Lounge","Hi-Fi Pizza & Giant Sub","Toast","Pyara Spa And Salon","Phoenix Landing","MexiCali Burrito","Nami Spa","Brattle Theatre","Bad Horse Pizza","Rao's Coffee","Uno Chicago Grill","Leisure Station","Club Passim","Voltage Coffee & Art","Black Ink","American Apparel","Roti Roll - Bombay Frankie","Columbia University","Pu Pu Hot Pot","Halo Pub","Mint Julep","Schoenhof's Foreign Books","Eastern Mountain Sports","Legal Sea Foods","Apple Tree Supermarket","Thailand Cafe","Hungry Mother","Hootenanny","b.good","The Enormous Room","Abigail's Restaurant","the bent spoon","Wegmans Food and Pharmacy","Boston Derby Dames","9 Tastes","Tommy Doyles Irish Pub & Restaurant","Dado Tea","Cardullo's Gourmet Shoppe","Oona's","The Field","Kendall Square Cinema","Wagamama","Eno Terra","John Harvard's Brew House","Amsterdam Tavern","Pasta E Basta","Beauty's","Karma Yoga Studio","First Printer","Harvard Book Store","Proletariat","Area Four","Bertucci's","V & T Pizzeria & Restaurant","Shalimar Of India Restaurant","Rangzen Tibetan Place","Sip","Clover Food Lab","Bistro Ten 18","Prana Power Yoga","Chuck's Spring Street Cafe","Pisticci","Izzy's Restaurant & Sub Shop","Lush","Charles Hotel","Middlesex Lounge","Raven Used Books","TT the Bear's Place","M2M","The Asgard Irish Pub & Restaurant","The Heights Bar & Grill","Sunny's Diner","Amherst Coffee","Shilla Korean & Japanese Restaurant","The Globe Corner Bookstore","Desi Dhaba","Max Café","Pepper Sky's Thai Sensation","Awash","Aceituna Cafe","The Village Pourhouse","Supreme Liquors","Manray","Conte's Bar","Firebrand Saints","Crossroads Irish Pub","Thelonious Monkfish","Nussbaum & Wu Bakery","Cuchi Cuchi","67 Orange Street","Crema Cafe","Leo's Place","Chipotle","Hubba Hubba","Sushi Palace","Hidden Sweets","Toscanini's Ice Cream","Miracle of Science Bar + Grill","Old World Pizza","Pearl Art & Craft Supplies","Terhune Orchards","ZuZu","Bub's BBQ","Koronet Pizza","Sezz Medi","Flat Patties","Cambridge, 1","The Blue Room","Spice Thai Cuisine","Russell House Tavern","Tea Magic","House of Cupcakes","The Garage","Sweet","Lizzy's Ice Cream","Harlem Tavern","BerryLine","Hamilton Deli","Hangar Pub & Grill","Sebastians Cafe & Catering","Central Bottle Wine + Provisions","Arrow Street Crêpes","Brookline Lunch","Lion's Head Tavern","Che' Bella Pizza","Fin's Sushi and Grill","Za","Rialto","Oren's Daily Roast","Harvard Film Archive","Zoma","Tortuga's Mexican Village","Central Square","Cambridge Brewing Company","The Garment District","ONE 53","Olives Deli & Bakery","Meadhall","Catalyst Restaurant","Café Kiraz","Moan & Dove","Upper Crust Pizzeria","Museum of Useful Things","Hong Kong At Harvard Square","Triumph Brewing Co","Veggie Planet","Whitney's Cafe","Harvest Co-Op Markets","Baraka Café","Urban Outfitters","Tanjore","Leavitt & Peirce Tobacco","Columbia Cottage","Alchemist & Barrister","Harvard Museum of Natural History","Absolute Bagels","Moody's Falafel Palace","Technique @ Le Cordon Bleu College of Culinary Arts","Chez Alice Cafe & Bakery","UBurger","Dolphin Seafood","ImprovBoston Theatre","Pinkberry","Bier International","Taqueria Y La Fonda","Broadway Marketplace","Lido","Casablanca Restaurant","Henrietta's Table","B-Side Lounge","Shalimar India Food & Spices","Hoagie Haven","Algiers Coffee House","Cosi","Border Café","Royal East Restaurant","Garden of Eden Gourmet","Vareli","West Bridge","Laverde's Market","LA Burdick Chocolate","Central Kitchen","Bob Slate Stationer","Elements","Flour Bakery + Café  Central Square","Ajihei","Harvard COOP","Bueno y Sano","Tomo Sushi of Princeton","Witherspoon Grill","Shanghai Park","Grafton Street","Princeton Record Exchange","Fire and Ice","Felipe's Taqueria","Anna's Taqueria","Teresa Caffe","Wai Lee Chinese Restaurant","Hungarian Pastry Shop","The Million Year Picnic","Flat Top Johnny's","Carberry's Bakery & Coffee House","The Tannery","Chameleon Tattoo & Body Piercing","Noir","The Friendly Toast","Cambridge Center Roof Garden","Atasca Hampshire","Bettolona","Redline","Finale","American Repertory Theater","OggiGourmet","Mel's Burger Bar","PJ's Pancake House Restaurant","Thomas Sweet Ice Cream","Miss Mamie's Spoonbread Too","Yenching Restaurant","Takemura Japanese Restaurant","The Cambridge Queen's Head","Vine: Sushi & Sake","Tommy Doyle's","Mediterra Restaurant","Falafel Corner","India Samraat","Westside Market NYC","Levain Bakery","Bertucci's Italian Restaurant - Kendall Square","Tom's Restaurant","The Middle East Restaurant And Nightclub","Havana Club","Charlie's Beer Garden","Teddy Shoes","The Red House","Witherspoon Bread Company","Make My Cake","Pinocchio's Pizza & Subs","Market In the Square","Tamarind Bay","Clear Conscience Cafe","Cinderella's Restaurant","Twist - Yogurt Without Limits","Zoe's","Z Square","Craigie On Main","Artopolis","Berk's","Peet's Coffee & Tea","Campo","The Dance Complex","MuLan","Clover HSQ","The Little Chef Pastry Shop","Thai Market","World's Only Curious George Store","Best Yet Market"
];

function split( val )
{
    return val.split( / \s*/ );
}

function extractLast( term ) 
{
    return split( term ).pop();
}

var myCenter;
var mynewCenter;

var directionsDisplay;
var directionsService = new google.maps.DirectionsService();
directionsDisplay = new google.maps.DirectionsRenderer();
var origin_lat=36.114588;
var origin_long=-115.161922;
var dest_lat;
var dest_long;


function calcRoute() {
  var selectedMode = document.getElementById("mode").value;
  var request = {
      origin: myCenter ,
      destination: mynewCenter,
      
      travelMode: google.maps.TravelMode[selectedMode]
  };
  directionsService.route(request, function(response, status) {
    if (status == google.maps.DirectionsStatus.OK) {
      directionsDisplay.setDirections(response);
  }
});
}
var l1=0;
var l2=0;
function success(position) {
 l1  = position.coords.latitude;
 l2 = position.coords.longitude;
 
 
 
 var validity =true;
 var valids=true;


 $('#street').on('input', function()
 {
    if (valids)
    {
        if ( $(this).val().trim() == "")
        {
            var i = $(this).attr('id') + "par";
            var abc = $(this).attr('id');$('#'+i).html("");
        }
        else 
        {
            var i = $(this).attr('id') + "par";var abc = $(this).attr('id');
            $('#'+i).html("&nbsp;"); 
        }
    }
});

 $('#street').bind( "keydown", function( event ) {

    if ( event.keyCode === $.ui.keyCode.TAB && $( this ).data( "autocomplete" ).menu.active ) 
    {
        event.preventDefault();
    }
}).autocomplete(
{
    minLength: 1,
    source: function( request, response ) 
    {
                // delegate back to autocomplete, but extract the last terms
                response( $.ui.autocomplete.filter(availableTags, extractLast( request.term ) ) );
            },

            focus: function() 
            {
                // prevent value inserted on focus
                return false;
            },

            select: function( event, ui ) 
            {
                var terms = split( this.value );
                // remove the current input
                terms.pop();
                // add the selected item
                terms.push( ui.item.value );
                // add placeholder to get the comma-and-space at the end
                terms.push( "" );
                this.value = terms.join( " " );
                return false;
            },

            open: function( event, ui ) 
            {
                var input = $( event.target ),
                widget = input.autocomplete( "widget" ),
                style = $.extend( input.css( [
                    "font", "border-left", "padding-left"] ), 
                {
                    position: "absolute",
                    visibility: "hidden",
                    "padding-right": 0,
                    "border-right": 0,
                    "white-space": "pre"
                } ),
                div = $( "<div/>" ),
                pos = {
                    my: "left top",
                    collision: "none"
                },
                offset = -7; // magic number to align the first letter
                // in the text field with the first letter
                // of suggestions
                // depends on how you style the autocomplete box

                widget.css( "width", "" );

                div
                .text( input.val().replace( /\S*$/, "" ) )
                .css( style )
                .insertAfter( input );
                offset = Math.min(
                    Math.max( offset + div.width(), 0 ),
                    input.width() - widget.width()
                    );
                div.remove();

                pos.at = "left+" + offset + " bottom";
                input.autocomplete( "option", "position", pos );

                widget.position( $.extend( { of: input }, pos ) );
            }
        });


$('#validateBtn').click(function(event) {
    $("#here_table").empty();
    $("#hello").empty();
    $("#googleMap").empty();

    validity =true;
    $('input[type="text"]').each(function() {
        if ($(this).val().trim() == "") {
            var i = $(this).attr('id') + "par";
            $('#'+i).html("Hey! You gotta give a query !");
            var abc = $(this).attr('id');



            validity=validity&false;
        }
        else {
            var i = $(this).attr('id') + "par";
            $('#'+i).html("&nbsp;"); 
            validity=validity&true;
            var abc = $(this).attr('id');



        }
    });

    valids=true;

                //l1= 36.114588;
                //l2 = -115.161922;

                if (validity)
                {
                    var formData = {
                        'query' : $('input[name=name]').val(),
                        'ranker' : 'comprehensive',
                        'latitude': l1,
                        'longitude':l2,

                    };

                    $.ajax({
                        type : 'GET', 
                        url:"http://linserv1.cims.nyu.edu:25808/search",
                        data : formData, 
                        dataType : 'json',
                        encode : true
                    })

                    .done(function(data)
                    {
//console.log(data["1"].address);
//console.log(Object.keys(data).length);




var mapProp = {
    zoom: 15,
    mapTypeId: google.maps.MapTypeId.ROADMAP
};

var map=new google.maps.Map(document.getElementById("googleMap"),mapProp);

directionsDisplay.setMap(map);

var image = new google.maps.MarkerImage('tac_business.png', new google.maps.Size(32,36), new google.maps.Point(0,0), new google.maps.Point(0,13));

if (navigator.geolocation)
{
    navigator.geolocation.getCurrentPosition(function(position) {
        myCenter = new google.maps.LatLng(position.coords.latitude,position.coords.longitude);
        //myCenter = new google.maps.LatLng(36.114588,-115.161922);
        map.setCenter(myCenter);
        var image_me = new google.maps.MarkerImage('tac_me.png', new google.maps.Size(32,36), new google.maps.Point(0,0), new google.maps.Point(0,13));
        var marker= new google.maps.Marker(
        {
            position: myCenter,
            icon: image_me,
            map: map,
            animation:google.maps.Animation.BOUNCE

        }
        ); 
    });
} 

else
{ 
    x.innerHTML = "Geolocation is not supported by this browser.";
}


var infowindow = null;
infowindow = new google.maps.InfoWindow({
 content: "holding..."
});

var content = "<table margin-left='10px;'>"
for(i=1; i<=Object.keys(data).length; i++){
    content += '<tr><td align="left" ><a href='+data[i].url+'>' + data[i].name + '</a></td></tr>';

    content += '<tr><td align="left" >'+ data[i].address+'</td></tr>';

    content += '<tr><td align="left" >STARS:' + data[i].star + '      No. of Reviews:'+ data[i].num_reviews+'</td></tr>';
    content += '<tr><td align="left" >      &nbsp; </td></tr>';
    content += '<tr><td align="left" >            &nbsp;       </td></tr>';

    var buisiness_coord= new google.maps.LatLng(data[i].lat,data[i].long);
    
    var marker= new google.maps.Marker(
    {
        position: buisiness_coord,
        icon: image,
        map: map,
        title: data[i].name,
        infowindow: infowindow,
        address: data[i].address,
        animation:google.maps.Animation.DROP
    }
    );

    google.maps.event.addListener(marker, 'click', function () {
      infowindow.setContent(this.title + '<br>' + this.address);
      infowindow.open(map, this);
      mynewCenter= this.position;
  });
    

}




content += "</table>"


var sd="<strong>Mode of Travel: </strong> <select id='mode' > <option value='DRIVING'>Driving</option> <option value='WALKING'>Walking</option> <option value='BICYCLING'>Bicycling</option><option value='TRANSIT'>Transit</option></select><button type='button' id='v' style='background-color:rgb(84,119,187);margin-left: 2%'class='btn btn-success' onclick='calcRoute();'>Get Directions</button>";



$('#here_table').append(content);
$('#hello').append(sd);
})

.fail(function(data) {
    console.log(data);
});

event.preventDefault();
}

event.preventDefault();
});
};

function error() {
    alert( "Unable to retrieve your location");
};




$(document).ready(function() 
{
    navigator.geolocation.getCurrentPosition(success, error);

    

});
