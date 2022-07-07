/* ------------------------------------------------------------------------------- 
   Window naming function to establish unique names.
   Replace dashes with underscores.
------------------------------------------------------------------------------- */
YAHOO.util.Event.addListener("enable_recurring_donations", "change", this.subForm);
function subForm(e)
{
	if (document.getElementById('enable_recurring_donations').checked) {
		document.getElementById('enable_recurring_donations').value="true";
	} else {
		document.getElementById('enable_recurring_donations').value="false";
	}
}

function windowNamer(thisURL) { 
   var name = 'popupWin_';
   var hash=0;
   for( i=0 ; i<thisURL.length ; i++){ hash+=thisURL.charCodeAt(i);}
   name += hash;
   return(name);
}

function openWindowWH(thisURL,thisW,thisH) {
   internalArgs = 'scrollbars,resizable,toolbar,status,left=50,top=50,width=' + thisW + ',height=' + thisH;       
   openWindow(thisURL,'popupWinWH',internalArgs);                                                                 
} 

function openWindow(internalURL,internalName,internalArgs) {
	if (internalURL == null || internalURL == '') {
		exit;
	}
	if (internalName == null || internalName == '') {
		internalName = 'popupWin';
	}
	if (internalArgs == null || internalArgs == '') {
		internalArgs = 'scrollbars,resizable,toolbar,status,width=640,height=480,left=50,top=50';
	}
	popupWin = window.open(internalURL,internalName,internalArgs);
 	popupWin.focus();
}

 function openWindowATC(thisURL,thisType,thisWidth,thisHeight,thisArgs,thisName) {
   if (thisType != '') {
      switch (thisType) {
         case 'demo':
            openWindowDemo(thisURL);
            break;
         case 'demosmall':
            openWindowDemo(thisURL);
            break;
         case '640':
            openWindow640(thisURL);
            break;
      }
   } else {
      if ((thisWidth != '') && (thisHeight != '')) {
         openWindowWH(thisURL,thisWidth,thisHeight);
      } else {
         openWindow(thisURL,thisName,thisArgs);
      }
   }                                                                                                              
} 

function openWindow640(thisURL) {
   openWindow(thisURL,'popupWin640','');
}

/*          
 * China Address: Select City based on State change
 */   
function putState()     {
  if (YAHOO.util.Dom.get("trigger_putState_CN_only")){
        var city = document.getElementById('shipping_city');
        var state = document.getElementById('shipping_state');
        var addr1 = document.getElementById('shipping_address1');

        if( !( city && state && addr1 )) return;

        txt = state.options[state.selectedIndex].text;

        if( state.selectedIndex == 1 ||
                 state.selectedIndex == 2 ||
                 state.selectedIndex == 3 ||
                 state.selectedIndex == 4 ||
                 state.selectedIndex == 33 ||
                 state.selectedIndex == 34 ) {
                        city.value = txt;
                        city.readOnly = true;
                        addr1.focus();
        } else {
                city.readOnly = false;
                city.value = "";
                city.focus();
        }
  }
}
   
function submitFormContainingField( formElementName, newValue ){
	var formIndex = FORM_INDEX_UNKNOWN = -1;
     
    for( var i = 0; i < document.forms.length; ++i ){
    	if( formIndex != FORM_INDEX_UNKNOWN ){ break; }
        for( var j = 0; j < document.forms[i].elements.length; ++j ){
        	if( document.forms[i].elements[j].name == formElementName ){
                     formIndex = i;
                     break;
            }
         }
	}
    if( formIndex != FORM_INDEX_UNKNOWN ){
    	//eval( 'document.forms[' + formIndex + '].' + formElementName ).value = newValue;
        //document.forms[formIndex].submit();
     
        return formIndex;
    }
}

/**
 * Quick fix for PPSCR00523682
 * dfltButton is needed when JS is disabled. 
 *
YAHOO.util.Event.addListener(window, 'load', function() {
	if (document.getElementById('dfltButton')) {
		var btn = document.getElementById('dfltButton');
		btn.parentNode.removeChild(btn);
	}
});*/
/* 18021 - display rewards tiers and update tracking var */
var trackView = function() {
	try {
		document.getElementById('rewards_tiers_views').value = 1;
	} catch(e) {};
}
YAHOO.util.Event.addListener(window,'load',function() {
		if (document.getElementById('currentfunding') && document.getElementById('switchnow')) {
			var switchRadio = document.getElementById('switchnow');
			var currentRadio = document.getElementById('currentfunding');
			currentRadio.previouslyChecked = currentRadio.checked;
			switchRadio.previouslyChecked = switchRadio.checked;
			YAHOO.util.Event.addListener([currentRadio,switchRadio],'click',switchNow);
		}
		if (document.getElementById('rewardsCallout')) {
			try {
				document.getElementById('rewardsCallout')._balloon.showEvent.subscribe(trackView);
			} catch(e) {}
		}
	});
var switchNow = function() {
	if (this.previouslyChecked != this.checked) {
		this.form.submit();
	}
}
YAHOO.util.Event.addListener("ita_applynow", "click", this.showHideITA);     
YAHOO.util.Event.addListener("currentfunding", "click", this.showHideITA);
function showHideITA(e)
{    
   obj= e.target || e.srcElement;
   if(obj.id=='ita_applynow')
   {    
	   YAHOO.util.Dom.removeClass("itawidget", "accessAid");
	   document.getElementById('itawidget').style.display="block"; 
	   YAHOO.util.Dom.addClass("ita", "applynowita");	
	   enablePayButtons(false);   
   }
   else if(obj.id=='currentfunding'){
	   YAHOO.util.Dom.addClass("itawidget", "accessAid");
	   YAHOO.util.Dom.removeClass("ita", "applynowita");
	   document.getElementById('itawidget').style.display="none";    
	   enablePayButtons(true);
   }
}

/**
    * Hide shipping section for non-referenced credit
    */
    PAYPAL.namespace("merchant.initiateCapture");
	
    PAYPAL.merchant.initiateCapture.hideShow = function(event){
	YAHOO.util.Event.preventDefault(event);
	YAHOO.util.Dom.replaceClass("initiateCapture", "toggleOpen", "toggleClose");
}
YAHOO.util.Event.addListener("initiateCaptureControl", "click", PAYPAL.merchant.initiateCapture.hideShow);

YAHOO.util.Event.addListener(window,'load',function() {
	if(YAHOO.util.Dom.get('leftSideBox') && YAHOO.util.Dom.get('control')) {
		var leftContainer = YAHOO.util.Dom.get('leftSideBox');
		leftContainerHeight = leftContainer.offsetHeight - 10;
		YAHOO.util.Dom.get('control').style.height=leftContainerHeight + "px";
	}
});

/* Canada C-28 */
YAHOO.util.Event.addListener(window,'load',function() {	
		if(document.getElementById("marketingEmailOptInlineMessage")) {
			var marketingEmailChkboxHideShow = new PAYPAL.widget.HideShow('marketingEmailOptInlineMessage', 'marketingEmailOpt');
			marketingEmailChkboxHideShow.toggleOpposite('marketingEmailOptInlineMessage');
			MarketingEmailOpt = YAHOO.util.Dom.get('marketingEmailOpt');
			if(MarketingEmailOpt && MarketingEmailOpt.checked){
				YAHOO.util.Dom.addClass('marketingEmailOptInlineMessage',"hide");
				}
		}
	});

YAHOO.util.Event.addListener(window,'load',function() {
	var dnFlow = document.getElementById("donationFlow");
	if(dnFlow) {
		var amField = document.getElementById("amount"),
		descField = document.getElementById("item_name"),
		recCboxField = document.getElementById("enable_recurring_donations"),
		amNode, recCboxNode, amount, descNode, tot1, tot2, tot3, currSep, currency, currencyCode, events, j;
		events = ['focus','blur','keypress','keydown','keyup','paste'];
		if(amField){
			amNode = document.createElement("input");
			amNode.type = "hidden";
			amNode.name = "amount";
			amNode.id = "shadowAmount";
			dnFlow.form.appendChild(amNode);
			amField.focus();
			YAHOO.util.Dom.addClass('update',"hide");
			YAHOO.util.Dom.removeClass('makeDonationMessage',"hide");
			tot1 = YAHOO.util.Dom.getElementsByClassName("item-total", "td")[0];
			tot2 = YAHOO.util.Dom.getElementsByClassName("totals-value", "td")[0];
			tot3 = document.getElementById("mainTotalAmount");
			currencyCode = YAHOO.util.Dom.getElementsByClassName("currCode", "td")[0].innerHTML;
			currSep = tot2.innerHTML.replace(/.*0([.,])00.*/g,"$1");
			currency = tot1.innerHTML;
			amNode.value = amField.value;
			var updateCurrency = function() {
				amField.value = amNode.value = amNode.value.replace(/^ *([.,][0-9]+) *$/g, "0$1");
				amount = amNode.value.search(/^ *(([0-9]+[.,]?)*[0-9]+) *$/);
				if(amount >= 0){
					tot1.innerHTML = currency + amNode.value;
					tot2.innerHTML = "<strong>" + currency + amNode.value + "</strong>";
					tot3.innerHTML = amNode.value;
				}
				else {
					if (currencyCode == 'JPY') {
						tot1.innerHTML = currency + "0";
						tot2.innerHTML = "<strong>" + currency + "0</strong>";
						tot3.innerHTML = "0";
					}
					else {
						tot1.innerHTML = currency + "0" + currSep + "00";
						tot2.innerHTML = "<strong>" + currency + "0" + currSep + "00</strong>";
						tot3.innerHTML = "0" + currSep + "00";
					}
				}
			};
			for(j=0; j < events.length; j++) {
				YAHOO.util.Event.addListener(amField, events[j], function(){
					amNode.value = amField.value;
				});
			}
			YAHOO.util.Event.addListener(amField, "blur", updateCurrency);
			updateCurrency();
		}
		if(descField){
			descNode = document.createElement("input");
			descNode.type = "hidden";
			descNode.name = "item_name";
			descNode.id = "shadowDescription";
			descNode.value = descField.value;
			dnFlow.form.appendChild(descNode);
			YAHOO.util.Dom.addClass('update',"hide");
			for(j=0; j < events.length; j++) {
				YAHOO.util.Event.addListener(descField, events[j], function(){
					descNode.value = descField.value;
				});
			}
		}
		if(recCboxField) {
                        recCboxNode = document.createElement("input");
                        recCboxNode.type = "hidden";
                        recCboxNode.name = "enable_recurring_donations";
                        recCboxNode.id = "enable_recurring_donations";
                        recCboxNode.value = recCboxField.value;
                        dnFlow.form.appendChild(recCboxNode);
                        YAHOO.util.Dom.addClass('update',"hide");
                        for(j=0; j < events.length; j++) {
                                YAHOO.util.Event.addListener(recCboxField, events[j], function(){
                                        recCboxNode.value = recCboxField.value;
                                });
                        }
                }
	}
});

function validateAmount(){
	/* this function syncs the shadow element with corresponding field value entered in the form */
	var aNode = document.getElementById("shadowAmount"),
	amnt = document.getElementById("amount"),
	dNode = document.getElementById("shadowDescription"),
	dVal = document.getElementById("item_name");
	if(aNode && amnt && amnt.value){
		aNode.value = amnt.value;
	}
	if(dNode && dVal && dVal.value){
		dNode.value = dVal.value;
	}
}

