
var x = document.getElementById("demo");
var abc;
var availableTags = [
"1020 Bar", "67 Orange Street", "9 Tastes", "A Cafe New York", "Abigail's Restaurant", "Absolute Bagels", "Aceituna Cafe", "Ajihei", "Alchemist & Barrister", "Algiers Coffee House", "All Asia Bar", "American Apparel", "American Repertory Theater", "Amherst Brewing Co", "Amherst Coffee", "Amsterdam Restaurant & Tapas Lounge", "Amsterdam Tavern", "Anna's Taqueria", "Antonio's", "Apple Tree Supermarket", "Area Four", "Arrow Street Crêpes", "Artist & Craftsman Supply", "Artopolis", "Atasca Hampshire", "Atkins Farms", "Awash", "B-Side Lounge", "Bad Horse Pizza", "Baraka Café", "Beauty's", "Beijing Tokyo", "Berk's", "BerryLine", "Bertucci's Italian Restaurant - Kendall Square", "Bertucci's", "Best Yet Market", "Bettolona", "Bier International", "Bistro Ten 18", "Black Ink", "Blockheads", "Blue Point Grill", "Bob Slate Stationer", "Boloco", "Bondir", "Border Café", "Boston Derby Dames", "Boston Tea Stop", "Brattle Square Florist", "Brattle Theatre", "Broadway Marketplace", "Brookline Lunch", "Bub's BBQ", "Bueno y Sano", "Cafe Pamplona", "Cafe Sushi", "Cafe of India", "Café 47", "Café Kiraz", "Café Luna", "Cambridge Bicycle", "Cambridge Brewing Company", "Cambridge Center Roof Garden", "Cambridge, 1", "Campo", "Carberry's Bakery & Coffee House", "Cardullo's Gourmet Shoppe", "Casablanca Restaurant", "Catalyst Restaurant", "Central Bottle Wine + Provisions", "Central Kitchen", "Central Square", "Chameleon Tattoo & Body Piercing", "Charles Hotel", "Charlie's Beer Garden", "Charlie's Kitchen", "Che' Bella Pizza", "Chez Alice Cafe & Bakery", "Chipotle Mexican Grill", "Chipotle", "Chuck's Spring Street Cafe", "Chutney's", "Cinderella's Restaurant", "Clear Conscience Cafe", "Clover Food Lab", "Clover HSQ", "Club Passim", "Columbia Cottage", "Columbia University", "Community Food & Juice", "Conte's Bar", "Corner Tavern", "Cosi", "Craigie On Main", "Crazy Dough's Pizza", "Crema Cafe", "Crepes on Columbus", "Crossroads Irish Pub", "Cuchi Cuchi", "Dado Tea", "Daedalus Restaurant & Pub", "Deluxe on Broadway", "Desi Dhaba", "Dolphin Seafood", "EVOO", "East Dumpling House", "Eastern Mountain Sports", "Elements", "Emma's Pizza", "Eno Terra", "Falafel Corner", "Felipe's Taqueria", "Ferry House", "Fin's Sushi and Grill", "Finale", "Fire and Ice", "Firebrand Saints", "First Printer", "Flat Patties", "Flat Top Johnny's", "Flour Bakery + Café  Central Square", "Fresh Side", "Fruity Yogurt", "Garden of Eden Gourmet", "Grafton Street", "Greek Corner Restaurant II", "Green Street", "Grendel's Den Restaurant & Bar", "Halo Pub", "Hamilton Deli", "Hangar Pub & Grill", "Harlem Tavern", "Harvard Book Store", "Harvard COOP", "Harvard Film Archive", "Harvard Museum of Natural History", "Harvard Square", "Harvest Co-Op Markets", "Harvest", "Havana Central", "Havana Club", "Henrietta's Table", "Herrell's Ice Cream", "Hi-Fi Pizza & Giant Sub", "Hi-Rise At the Blacksmith House", "Hidden Sweets", "Hoagie Haven", "Hong Kong At Harvard Square", "Hootenanny", "House of Cupcakes", "Hubba Hubba", "Hungarian Pastry Shop", "Hungry Mother", "IHOP", "ImprovBoston Theatre", "India Pavilion Restaurant", "India Samraat", "Izzy's Restaurant & Sub Shop", "JP Licks", "John Harvard's Brew House", "Judie's", "Karma Yoga Studio", "Kendall Square Cinema", "Kitchenette Uptown", "Koronet Pizza", "LA Burdick Chocolate", "Laverde's Market", "Le Monde", "Le's Restaurant", "Leavitt & Peirce Tobacco", "Legal Sea Foods", "Legal Sea Foods", "Leisure Station", "Leo's Place", "Levain Bakery", "Lido", "Lion's Head Tavern", "Lizzy's Ice Cream", "Loews Harvard Square", "Lord Hobo", "Lush", "Lyndell's Bakery", "M2M", "MIT Museum", "Make My Cake", "Manray", "Maoz Vegetarian", "Mariposa Bakery", "Market In the Square", "Mary Chung Restaurant", "Massachusetts Institute of Technology", "Massawa", "Max Café", "Max Soha", "Meadhall", "Mediterra Restaurant", "Mel's Burger Bar", "Melba's", "MexiCali Burrito", "Middlesex Lounge", "Milano Market", "Mill Korean", "Mint Julep", "Miracle of Science Bar + Grill", "Miss Mamie's Spoonbread Too", "Moan & Dove", "Moody's Falafel Palace", "Mr. Bartley's Burger Cottage", "MuLan", "Museum of Useful Things", "Nami Spa", "Newbury Comics", "Noir", "Nussbaum & Wu Bakery", "ONE 53", "OggiGourmet", "Old World Pizza", "Olives Deli & Bakery", "Om Restaurant & Lounge", "Oona's", "Oren's Daily Roast", "Otto Pizza", "PARK Restaurant & Bar", "PJ's Pancake House Restaurant", "Pasta E Basta", "Patisserie Des Ambassades", "Pearl Art & Craft Supplies", "Peet's Coffee & Tea", "Pepper Sky's Thai Sensation", "Phoenix Landing", "Pinkberry", "Pinocchio's Pizza & Subs", "Pisticci", "Prana Power Yoga", "Princeton Record Exchange", "Proletariat", "Pu Pu Hot Pot", "Pyara Spa And Salon", "Qdoba", "Rack & Soul", "Rangzen Tibetan Place", "Rao's Coffee", "Raven Used Books", "Redline", "Rendezvous In Central Square", "Rialto", "Roti Roll - Bombay Frankie", "Royal East Restaurant", "Russell House Tavern", "Sakura Express", "Salts Restaurant", "Sandrine's", "Schoenhof's Foreign Books", "Sebastians Cafe & Catering", "Sezz Medi", "Shabu-Ya", "Shalimar India Food & Spices", "Shalimar Of India Restaurant", "Shanghai Park", "Shays Pub & Wine Bar", "Shilla Korean & Japanese Restaurant", "Sip", "Small World Coffee", "Society Coffee", "Spice Thai Cuisine", "SubsConscious", "Sugar+Sunshine Bakery", "Suma Sushi", "Sunny's Diner", "Supreme Liquors", "Sushi Palace", "Sweet", "Sweet", "TT the Bear's Place", "Takemura Japanese Restaurant", "Tamarind Bay", "Tanjore", "Taqueria Y La Fonda", "Tea Magic", "Tealuxe", "Technique @ Le Cordon Bleu College of Culinary Arts", "Teddy Shoes", "Teresa Caffe", "Terhune Orchards", "Thai Market", "Thailand Cafe", "The Asgard Irish Pub & Restaurant", "The Blue Room", "The Cambridge Queen's Head", "The Cathedral Church of Saint John the Divine", "The Dance Complex", "The Enormous Room", "The Field", "The Friendly Toast", "The Garage", "The Garment District", "The Globe Corner Bookstore", "The Heights Bar & Grill", "The Little Chef Pastry Shop", "The Middle East Restaurant And Nightclub", "The Million Year Picnic", "The Muddy Charles Pub at MIT", "The Red House", "The Tannery", "The Village Pourhouse", "Thelonious Monkfish", "Think Tank", "Thomas Sweet Ice Cream", "Toast", "Tom's Restaurant", "Tommy Doyle's", "Tommy Doyles Irish Pub & Restaurant", "Tomo Sushi of Princeton", "Tortuga's Mexican Village", "Tory Row", "Toscanini's Ice Cream", "Trata", "Triumph Brewing Co", "Twist - Yogurt Without Limits", "UBurger", "Uno Chicago Grill", "Upper Crust Pizzeria", "Upstairs On the Square", "Urban Outfitters", "V & T Pizzeria & Restaurant", "Vareli", "Veggie Galaxy", "Veggie Planet", "Vine: Sushi & Sake", "Voltage Coffee & Art", "Wagamama", "Wai Lee Chinese Restaurant", "Wegmans Food and Pharmacy", "West Bridge", "Westside Market NYC", "Whitney's Cafe", "Winberie's Restaurant & Bar", "Witherspoon Bread Company", "Witherspoon Grill", "Wondee Siam V", "World's Only Curious George Store", "Yenching Restaurant", "Z Square", "Za", "Zoe's", "Zoma", "ZuZu", "the bent spoon"
];
var availableCitys = [
"Current Location",
"Morningside Heights, NY",
"Ithaca, NY",
"Troy, NY",
"Albany, NY",
"Princeton, NJ",
"Philadelphia, PA",
"Pittsburgh, PA",
"Phoenix, AZ",
"Scottsdale, AZ",
"Mesa, AZ",
"Las Vegas, NV",
"Henderson, NV",
"Madison, WI",
"Ann Arbor, MI ",
"Boston, MA",
"Cambridge, MA",
"Amherst, MA",
"Los Angeles, CA",
"Berkeley, CA",
"Pasadena, CA",
"Austin, TX",
"Houston, TX"
];

function split( val ) {
    return val.split( / \s*/ );
}

function extractLast( term )  {
    return split( term ).pop();
}

var myCenter;
var mynewCenter;

var directionsDisplay = new google.maps.DirectionsRenderer();
var directionsService = new google.maps.DirectionsService();
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

    $('#autoQry').on('input', function() 
    {
        if (valids) {
            if ( $(this).val().trim() == "") {
                var i = $(this).attr('id') + "par";
                var abc = $(this).attr('id');$('#'+i).html("");
            }
            else {
                var i = $(this).attr('id') + "par";
                var abc = $(this).attr('id');
                $('#'+i).html("&nbsp;"); 
            }
        }
    });

    //---------- AUTO COMPLETE Location ----------------- //
    $('#autoLoc').bind( "keydown", function( event ) {
        if ( event.keyCode === $.ui.keyCode.TAB && $( this ).data( "autocomplete" ).menu.active ) {
            event.preventDefault();
        }
    }).autocomplete({ 
            minLength: 1,
            source: function( request, response ) {
                // delegate back to autocomplete, but extract the last terms
//                response( $.ui.autocomplete.filter(availableTags, extractLast( request.term ) ) );
                response( $.ui.autocomplete.filter(availableCitys, request.term ) );
            },
            focus: function() {
                // prevent value inserted on focus
                return false;
            },
           select: function( event, ui ) {
//                var terms = split( this.value );
                var terms = [this.value];
                // remove the current input
                terms.pop();
                // add the selected item
                terms.push( ui.item.value );
                // add placeholder to get the comma-and-space at the end
                terms.push( "" );
                this.value = terms.join( " " );
                return false;
            },
            open: function( event, ui ) {
                var input = $( event.target ),
                widget = input.autocomplete( "widget" ),
                style = $.extend( input.css( [ "font", "border-left", "padding-left"] ), 
                                    {
                                        position: "absolute",
                                        visibility: "hidden",
                                        "padding-right": 0,
                                        "border-right": 0,
                                        "white-space": "pre"
                                    } 
                                ),
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
    //------END---- AUTO COMPLETE Location -------END---------- //


    //---------- AUTO COMPLETE BUSINESS NAME ----------------- //
    $('#autoQry').bind( "keydown", function( event ) {
        if ( event.keyCode === $.ui.keyCode.TAB && $( this ).data( "autocomplete" ).menu.active ) {
            event.preventDefault();
        }
    }).autocomplete({ 
            minLength: 1,
            source: function( request, response ) {
                // delegate back to autocomplete, but extract the last terms
//                response( $.ui.autocomplete.filter(availableTags, extractLast( request.term ) ) );
                response( $.ui.autocomplete.filter(availableTags, request.term ) );
            },
            focus: function() {
                // prevent value inserted on focus
                return false;
            },
           select: function( event, ui ) {
//                var terms = split( this.value );
                var terms = [this.value];
                // remove the current input
                terms.pop();
                // add the selected item
                terms.push( ui.item.value );
                // add placeholder to get the comma-and-space at the end
                terms.push( "" );
                this.value = terms.join( " " );
                return false;
            },
            open: function( event, ui ) {
                var input = $( event.target ),
                widget = input.autocomplete( "widget" ),
                style = $.extend( input.css( [ "font", "border-left", "padding-left"] ), 
                                    {
                                        position: "absolute",
                                        visibility: "hidden",
                                        "padding-right": 0,
                                        "border-right": 0,
                                        "white-space": "pre"
                                    } 
                                ),
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
    //------END---- AUTO COMPLETE BUSINESS NAME -------END---------- //


    $('#validateBtn').click(function(event) {
        $("#here_table").empty();
        $("#hello").empty();
        $("#googleMap").empty();

        validity =true;
        $('#autoQry').each(function() {
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

        var location = $.trim($('input[name=loc]').val());
        //console.log(location);
        switch (location) {
            case "Morningside Heights, NY":
                l1= 40.8089564;
                l2= -73.9624327;
                break;
            case "Phoenix, AZ":
                l1= 33.448377;
                l2= -112.074037;
                break;
            case "Las Vegas, NV":
                l1=36.114646;
                l2=-115.172816;
                break;
            case "Henderson, NV":
                l1=36.033669;
                l2=-115.002364;
                break;
            case "Madison, WI":
                l1=43.0730517;
                l2=-89.4012302;
                break;
            case "Ann Arbor, MI":
                l1=42.2708716;
                l2=-83.7263294;
                break;
            case "Philadelphia, PA":
                l1=39.952335;
                l2=-75.163789;
                break;
            case "Pittsburgh, PA":
                l1=40.4406248;
                l2=79.9958864;
                break;
            case "Amherst, MA":
                l1=42.3803676;
                l2=-72.523143;
                break;
            case "Boston, MA":
                l1=42.3584308;
                l2=-71.0597732;
                break;
            case "Cambridge, MA":
                l1=42.3726399;
                l2=-71.1096528;
                break;
            case "Princeton, NJ":
                l1=40.3487181;
                l2=-74.6590472;
                break;
            case "Los Angeles, CA":
                l1=34.0522342;
                l2=-118.2436849;
                break;
            case "Berkeley, CA":
                l1=37.8900401;
                l2=-122.2715061;
                break;
            case "San Luis Obispo, CA":
                l1=35.2827524;
                l2=-120.6596156;
                break;
            case "Pasadena, CA":
                l1=34.1477849;
                l2=-118.1445155;
                break;
            case "Scottsdale, AZ":
                l1=33.4941704;
                l2=-111.9260519;
                break;
            case "Mesa, AZ":
                l1=33.4222685;
                l2=-111.8226402;
                break;
            case "Ithaca, NY":
                l1=42.4433333;
                l2=-76.5;
                break;
            case "Troy, NY":
                l1=42.7284117;
                l2=-73.6917851;
                break;
            case "Albany, NY":
                l1=42.6525793;
                l2=-73.7562317;
                break;
            case "Austin, TX":
                l1=30.267153;
                l2=-97.7430608;
                break;
            case "Houston, TX":
                l1=29.7604267;
                l2=-95.3698028;
                break;
            default:
                l1= position.coords.latitude;
                l2= position.coords.longitude;
                break;
        }

        var searchType = $('button[name=qryType]').val();
        var fsim;
        var flike;
        if (searchType == "Business") {
            fsim = "no";
            flike = "no";
        }
        else {
            if (searchType == "Similar"){
                fsim = "yes";
                flike = "no";
            }
            else {
                fsim = "no";
                flike = "yes";
            }
        }

        if (validity) {
            var formData = {
                'query' : $('input[name=name]').val(),
                'ranker' : 'comprehensive',
                'latitude': l1,
                'longitude':l2,
                'findsim': fsim,
                'findlike': flike,
            };
            $.ajax({
                type : 'GET', 
                url:"http://linserv2.cims.nyu.edu:25808/search",
                data : formData, 
                dataType : 'json',
                encode : true
            })
           .done(function(data) {
                //console.log(data["1"].address);
                //console.log(Object.keys(data).length);
                var mapProp = {
                    zoom: 15,
                    mapTypeId: google.maps.MapTypeId.ROADMAP
                };
                var map=new google.maps.Map(document.getElementById("googleMap"),mapProp);
                directionsDisplay.setMap(map);
                var image = new google.maps.MarkerImage('tac_business.png', new google.maps.Size(32,36), new google.maps.Point(0,0), new google.maps.Point(0,13));

                if (navigator.geolocation) {
                    navigator.geolocation.getCurrentPosition(function(position) {
                        myCenter = new google.maps.LatLng(l1, l2);
                        //myCenter = new google.maps.LatLng(36.114588,-115.161922);
                        map.setCenter(myCenter);
                        var image_me = new google.maps.MarkerImage('tac_me.png', new google.maps.Size(32,36), new google.maps.Point(0,0), new google.maps.Point(0,13));
                        var marker= new google.maps.Marker( {
                            position: myCenter,
                            icon: image_me,
                            map: map,
                            animation:google.maps.Animation.BOUNCE
                        }); 
                    });
                } 
                else { 
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

$(function(){

    $(".dropdown-menu li a").click(function(){

      $(".btn:first-child").text($(this).text());
      $(".btn:first-child").val($(this).text());

   });

});

$(document).ready(function() 
{
    navigator.geolocation.getCurrentPosition(success, error);

    

});
