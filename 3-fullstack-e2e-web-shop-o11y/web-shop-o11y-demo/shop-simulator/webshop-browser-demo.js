import { chromium } from 'k6/x/browser';
import exec from 'k6/execution';
import { sleep } from 'k6';
import { check } from 'k6';

let user= "Emil";

//export const options = {
//   scenarios: {
//     messages: {
//       executor: 'constant-vus',
//       exec: 'browser',
//       vus: 1,
//       duration: '1m',
//     },
//   },
// };

export default function() {
  const browser = chromium.launch({
    headless: false,
    slowMo: '500ms',
  });

  const context = browser.newContext({
        screen: {width: 1024, height: 768},
        viewport: { width: 1024, height: 768}
  });
  const page = context.newPage();
  page.goto('http://grafana.datahovel.com:3389/shop?name='+user);


  let selector, elem;

  page.mouse.click(344, 402);
  sleep(1);
  page.mouse.click(530, 410);
  sleep(1);

  selector='[href="/cart?name='+user+'"]';
  elem = page.$(selector);
  elem.click();
  sleep(1);

  selector='.w3-main';
  elem = page.$(selector);

  let re= /Loki\s*(.*)\s*(.*)\s*(.*)\s*Meows\s*(.*)\s*(.*)\s*(.*)\s*/;
  let match = elem.textContent().match(re);
  if(match== null) {
    re= /Meows\s*(.*)\s*(.*)\s*(.*)\s*Loki\s*(.*)\s*(.*)\s*(.*)\s*/;
    match = elem.textContent().match(re);
  }

  let total= Number(match[3])+Number(match[6]);
  console.log("Total: "+total);

  check(page, { in: "69.98"== total});

  sleep(1);

//  page.screenshot({ path:"kitties.png" });

  selector="[id='myBtn']";
  elem = page.$(selector);
  elem.click();
  sleep(1);
  elem.click();
  sleep(1);

  selector='[name="checkout_cart"]';
  elem = page.$(selector);
  elem.click();

  selector="[onclick='do_something_cool()']";
  elem = page.$(selector);
  elem.click();
  sleep(1);


  page.close();
  browser.close();
}
