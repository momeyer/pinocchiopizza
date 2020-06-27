toppings = {
    'Cheese': 1,
    'One topping': 2,
    'Two toppings': 3,
    'Three toppings': 4,
    'Special': 5,
}

$(document).ready(() => {

    console.log(urlOrderPizza)
    console.log(urlOrderSub)
    console.log(urlOrderSalad)
    console.log(urlOrderPasta)
    console.log(urlOrderDinner)
    console.log(urlRemoveItem)

    console.log('ready')
    // submition buttons
    var regular_pizza_button = $("#add_regular_pizza_button")
    var sicilian_pizza_button = $("#add_sicilian_pizza_button")
    var sub_button = $("#add_sub")
    var pasta_button = $("#add_pasta")
    var salad_button = $("#add_salad")
    var dinner_button = $("#add_dinner")
    var payButton = $("#playment")

    // related to Pizzas only
    var modal = $("#pizza")
    var regularTop = $("#regular_toppings")
    var regularQnt = $("#regular_qnt")
    var regularSize = $("#regular_size")

    var sicilianTop = $("#sicilian_toppings")
    var sicilianQnt = $("#sicilian_num")
    var sicilianSize = $("#sicilian_size")

    var sub = $("#sub")
    var extra = $("[name='extra']")
    var subSize = $("#sub_size")
    var subQnt = $("#sub_qnt")

    var pasta = $("#pasta")
    var pastaQnt = $("#pasta_qnt")

    var salad = $("#salad")
    var saladQnt = $("#salad_qnt")

    var dinner = $("#dinner")
    var dinnerSize = $("#dinner_size")
    var dinnerQnt = $("#dinner_qnt")

    var items = $(".items_div")
    var total = $(".totalPrice")


    // payment info
    var street = $("#inputAddress")
    var state = $("#inputState") 
    var city = $("#inputCity")
    var zipcode = $("#inputZip")
    var checkoutModal = $("#checkoutModal")
    var deliveryModal = $("#deliveryInfo")



    payButton.click( () => {
        console.log("pay")
        console.log(street.val(), state.val(), city.val(), zipcode.val())
        
        data = {
            "street" : street.val(),
            "state" : state.val(),
            "city" : city.val(),
            "zip" : zipcode.val(),
        }

        $.ajax(
            {
                type: "POST",
                url: urlCheckout,
                data: data,
                success: function (data) {
                    $("#delivery_name").html(data.username)
                    $("#delivery_address").html(data.address)
                    $("#delivery_time").html(data.delivery_time)
                    deliveryModal.modal('show')
                },
                error: function () {
                    alert("error, please try again")
                }
            })

        checkoutModal.modal("hide")
    }

    )


    regular_pizza_button.click(() => {
        if (regularQnt.val() < 1){
            qnt = 1;
        } else {
            qnt = regularQnt.val()
        }

        dataPizza = {
            "regular_toppings": regularTop.val(),
            "size": regularSize.val(),
            "num": qnt,
            'top_opt': []

        }
        if (regularTop.val() !== 'Cheese' && regularTop.val() !== 'Special') {
            modal.modal('show')
            limitToppings(toppings[regularTop.val()])
        }
        else {
            if (regularTop.val() === 'Cheese')
            {
                $("#add_pizza").click()
            }
            if (regularTop.val() === 'Special')
            {
                dataPizza.top_opt.push('Cheff will prepere something special.')
                $("#add_pizza").click()
            }
        }


    });

   

    sicilian_pizza_button.click(() => {
        if (sicilianQnt.val() < 1){
            qnt = 1;
        } else {
            qnt = sicilianQnt.val()
        }
        dataPizza = {
            "sicilian_toppings": sicilianTop.val(),
            "size": sicilianSize.val(),
            "num": qnt,
            'top_opt': []

        }
        if (sicilianTop.val() !== 'Cheese' && sicilianTop.val() !== 'Special') {
            modal.modal('show')
            limitToppings(toppings[sicilianTop.val()])
        }
        else {
            if (sicilianTop.val() === 'Cheese')
            {
                $("#add_pizza").click()
            }
            if (sicilianTop.val() === 'Special')
            {
                dataPizza.top_opt.push('Cheff will prepere something special.')
                $("#add_pizza").click()
            }
        }
    });

    $("#add_pizza").click(() => {
        $('input:checkbox[name=top_opt]').each(function () {
            if ($(this).is(':checked')) {
                dataPizza.top_opt.push($(this).val())
                $(this).prop("checked", false);
            }
        });

        makeAjaxRequest(urlOrderPizza, dataPizza)

    })

    
    sub_button.click(() => {

        if (subQnt.val() < 1){
            qnt = 1;
        } else {
            qnt = subQnt.val()
        }

        dataSub = {
            "sub": sub.val(),
            "size": subSize.val(),
            "num": qnt,
            'extra': extra.val()
        }
        makeAjaxRequest(urlOrderSub, dataSub)

    });

    pasta_button.click(() => {

        if (pastaQnt.val() < 1){
            qnt = 1;
        } else {
            qnt = pastaQnt.val()
        }

        dataPasta = {
            "pasta": pasta.val(),
            "num": qnt,
        }
        makeAjaxRequest(urlOrderPasta, dataPasta)

    });


    salad_button.click(() => {

        if (saladQnt.val() < 1){
            qnt = 1;
        } else {
            qnt = saladQnt.val()
        }

        dataSalad = {
            "salad": salad.val(),
            "num": qnt,
        }
        makeAjaxRequest(urlOrderSalad, dataSalad)

    });

    dinner_button.click(() => {

        if (dinnerQnt.val() < 1){
            qnt = 1;
        } else {
            qnt = dinnerQnt.val()
        }
        dataDinner = {
            "dinner": dinner.val(),
            "size": dinnerSize.val(),
            "num": qnt,
        }
        makeAjaxRequest(urlOrderDinner, dataDinner)

    });

    function makeAjaxRequest(url, data) {

        $.ajax(
            {
                type: "POST",
                url: url,
                data: data,
                success: function (data) {
                    divElement = `
                    <div class="${data.itemId}_item_div">
                        <div style="margin-top: 5px;">${data.qnt}x ${data.itemName} US$ ${data.price}
                            <button class="trash" id="${data.itemId}" onclick="deleteItem(this.id)">
                                <svg class="bi bi-trash" width="1.5em " height="1em" viewBox="0 0 16 16" fill="white" xmlns="http://www.w3.org/2000/svg">
                                    <path d="M5.5 5.5A.5.5 0 016 6v6a.5.5 0 01-1 0V6a.5.5 0 01.5-.5zm2.5 0a.5.5 0 01.5.5v6a.5.5 0 01-1 0V6a.5.5 0 01.5-.5zm3 .5a.5.5 0 00-1 0v6a.5.5 0 001 0V6z" />
                                    <path fill-rule="evenodd" d="M14.5 3a1 1 0 01-1 1H13v9a2 2 0 01-2 2H5a2 2 0 01-2-2V4h-.5a1 1 0 01-1-1V2a1 1 0 011-1H6a1 1 0 011-1h2a1 1 0 011 1h3.5a1 1 0 011 1v1zM4.118 4L4 4.059V13a1 1 0 001 1h6a1 1 0 001-1V4.059L11.882 4H4.118zM2.5 3V2h11v1h-11z" clip-rule="evenodd" />
                                </svg>
                            </button>
                        </div>`
                    if (data.toppings !== undefined && data.toppings !== "none") {
                        divElement += `<div class="size_div">${data.toppings}</div>`
                    }
                    if (data.size !== undefined) {
                        divElement += `<div class="size_div">size: ${data.size}</div>`
                    }

                    divElement += "</div>"

                    items.append(divElement)
                    modal.modal('hide')

                    total.html(data.total)
                },
                error: function () {
                    alert("error, please try again")
                }
            })
    }
});



function limitToppings(toppings) {
    $('.form-check-input').attr('disabled', false)
    $('.form-check-input').on('change', function () {
        var noChecked = 0;
        $.each($('.form-check-input'), function () {
            if ($(this).is(':checked')) {
                noChecked++;
            }
        });
        if (noChecked >= (toppings - 1)) {
            $.each($('.form-check-input'), function () {
                if ($(this).not(':checked').length == 1) {
                    $(this).attr('disabled', 'disabled');
                }
            });
        } else {
            $('.form-check-input').removeAttr('disabled');
        };
    });
}

function deleteItem(id) {
    console.log("deleting iteems")
    var total = $(".totalPrice")
    data = {
        "itemId": id
    }
    $.ajax(
        {
            type: "POST",
            url: urlRemoveItem,
            data: data,
            success: function (data) {
                total.html(data.total)
                $(`.${data.itemId}_item_div`).remove()
            }
        })
}

