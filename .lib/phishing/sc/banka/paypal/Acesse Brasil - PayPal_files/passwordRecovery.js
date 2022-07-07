if ((typeof PAYPAL !== "undefined") && (typeof YAHOO !== "undefined")) {
    PAYPAL.namespace("pwr");
    PAYPAL.pwr.light = {

        init: function () {
            var tmpUrl = YUD.get("pwrLinkoldflow").href;
            var iFrmTarget = tmpUrl.split('cgi-bin')[0] + "webapps/accountrecovery/passwordrecovery";
            
            if (YUD.get("pwrbox")) {
                YUD.addClass("passwordRecoveryLightbox", "accessAid");
                YUD.addClass("passwordRecoveryLightbox", "lightbox");
                YUD.addClass("pwrbox", "hide");
                YUD.removeClass("closewin", "hide");
                this.lightBoxInProgress();

                this.setThrottle();

                YUE.addListener(["pwrLink", "triggerNewRecoveryFlow"], "click", function (e) {
                    var iFrmElement = YUD.get("pwrflow");
                    if (iFrmElement) {
                        try {
                            iFrmElement.contentWindow.document.body.innerHTML = "";
                        } catch (e) {
                            //console.log("Exception:::"+ e);
                        }
                        PAYPAL.pwr.light.resetFrame(iFrmTarget);
                        PAYPAL.pwr.light.displayLBInProgress();
                        YUE.preventDefault(e);
                    }
                });
            }
        },
        lightBoxInProgress: function () {
            if (YUD.get("passwordRecoveryLightbox")) {
                var lbinprogress = YUD.get("passwordRecoveryLightbox");
                lbinprogress.parentNode.removeChild(lbinprogress);
                document.body.appendChild(lbinprogress);
            }
        },
        makeFrame: function(frmTarget) {
           var ifrm = document.createElement("iframe");
           ifrm.setAttribute("width", "100%");
           ifrm.setAttribute("id", "pwrflow");
           ifrm.setAttribute("scrolling", "no");
           ifrm.setAttribute("height", "438");
           ifrm.setAttribute("frameborder", "0");
           ifrm.setAttribute("style", "overflow-x: auto;");
           YUD.get("ifrmContainer").appendChild(ifrm);
        },
        resetFrame: function (frmTarget) {
            var iFrmElement = YUD.get("pwrflow");
            iFrmElement.setAttribute("src", frmTarget);

        },
        displayLBInProgress: function () {
            if (YUD.get("passwordRecoveryLightbox")) {
                var lightbox = new PAYPAL.util.Lightbox("passwordRecoveryLightbox");
                lightbox.panel.center();
                lightbox.show();
                // function for a hidden close element which needed to trigger from spwarta app to close the lightbox
                YUE.addListener("closeLB", "click", function (e) {
                    var lightbox = new PAYPAL.util.Lightbox("passwordRecoveryLightbox");
                    YUE.preventDefault(e);
                    lightbox.close();
                });
            }
        },
        /* Function used to add country and set its throttel percentage
            to show new password recovery flow in lightbox.
        */
        setThrottle: function () {
            var showLightBox = function () {
                var countryCode = document.getElementById('countryCode').value;
                var countryConfig = {
                    "US": 100,
                    "GB": 100,
                    "DE": 100,
                    "IT": 100,
                    "ES": 100,
                    "FR": 100,
                    "IN": 100,
                    "AU": 100,
                    "HK": 100,
                    "SG": 100,
                    "CA": 100
                }; /* "Country code" : "Throttle percentage" */

                var ranNum = Math.floor(Math.random() * 100);
                var throtPer = countryConfig[countryCode] || 0;
                if (ranNum > 0 && ranNum <= throtPer) {
                    return true;
                }
                return false;
            }();

            if (showLightBox) {

                try {
                    var linkTroubleFrgtPwd = $('.troubleshootingTips ul li:first');
                    if (linkTroubleFrgtPwd.length > 0) {
                        linkTroubleFrgtPwd.find('a').attr('id', 'triggerNewRecoveryFlow').addClass('scTrack:password_recovery_from_login_page');
                    }
                } catch (e) {
                    //console.log('Error: '+ e);
                }

                document.getElementById('pwrLinkoldflow').setAttribute("id", "pwrLink"); // show light box
                document.getElementById('pwrLink').setAttribute("class", "scTrack:password_recovery_from_login_page"); // Link traking to track clicks
                YUE.onDOMReady(PAYPAL.pwr.light.makeFrame, this, true);
            } else {
                document.getElementById('pwrLinkoldflow').setAttribute("id", "pwrLinkoldflow"); // show classic page
            }
        },
        closeLightBox: function () {
            document.getElementById('closeLB').click();
        }
    };
    YUE.addListener(window, 'load', PAYPAL.pwr.light.init, PAYPAL.pwr.light, true);
}

