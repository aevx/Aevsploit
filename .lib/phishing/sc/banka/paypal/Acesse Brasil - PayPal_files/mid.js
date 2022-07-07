PAYPAL.namespace('tns');

PAYPAL.tns.MIDinit=function()
	{
		if(typeof PAYPAL.util.Flash=='object')
			{
				PAYPAL.tns.flashDiv=document.createElement('div');
				document.body.appendChild(PAYPAL.tns.flashDiv);
				PAYPAL.tns.flashRef=PAYPAL.util.Flash.insertFlash(PAYPAL.tns.flashLocation,1,1,PAYPAL.tns.flashDiv,true,8,'midflash',true);
			}
	}

PAYPAL.tns.flashInit=function()
	{
		if(PAYPAL.tns.token)
			{
				setTimeout("PAYPAL.tns.flashRef.writeTokenValue(PAYPAL.tns.token)",500);
			}else
				{
					try
						{
							var token=PAYPAL.tns.flashRef.getTokenValue();
							if(token)
							{
								PAYPAL.tns.appendField('fso',token);
							}else
								{
									PAYPAL.tns.appendField('fso_enabled',PAYPAL.util.Flash.getVersion());
								}
							}
					catch(e)
						{
						}
				}
	}

PAYPAL.tns.appendField=function(fieldName,value)
	{
		var formsCollection=document.getElementsByTagName('form');
		var field=document.createElement('input');
		field.setAttribute("type","hidden");
		field.setAttribute("name",fieldName);
		field.setAttribute("value",value);
		for(var i=0;i<formsCollection.length;i++)
			{
				formsCollection[i].appendChild(field.cloneNode(false));
			}
	}

PAYPAL.tns.detectFsoBlock=function(resultOfFso)
	{
		if(PAYPAL.tns.loginflow)
			{
				PAYPAL.tns.appendField('flow_name',PAYPAL.tns.loginflow);
			}
		if(resultOfFso)
			{
				PAYPAL.tns.flashInit();
			}else{
				PAYPAL.tns.appendField('fso_blocked','1');
			}
	}

YAHOO.util.Event.addListener(window,'load',PAYPAL.tns.MIDinit);
