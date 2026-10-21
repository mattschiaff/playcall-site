// Load the official provider widget only after the visitor's intentional action.
// Subscription, errors and double opt-in remain owned by MailerLite.
const button=document.querySelector('[data-load-waitlist]');
if(button)button.addEventListener('click',()=>{
 if(button.disabled)return;button.disabled=true;
 const target=document.querySelector('#mailerlite-mount'),status=document.querySelector('#waitlist-status'),template=document.querySelector('#mailerlite-template');
 status.textContent='Loading the MailerLite email form…';
 target.append(template.content.cloneNode(true));
 for(const old of target.querySelectorAll('script')){const script=document.createElement('script');for(const a of old.attributes)script.setAttribute(a.name,a.value);script.textContent=old.textContent;old.replaceWith(script)}
 const observer=new MutationObserver(()=>{
  if(target.querySelector('input[name="fields[email]"]')){status.textContent='Complete the signup form below, then check your email to confirm.';button.hidden=true;
   const email=target.querySelector('input[name="fields[email]"]'),consent=target.querySelector('input[type="checkbox"]'),errors=document.querySelector('#waitlist-errors');
   if(email){email.id='playcall-waitlist-email';email.required=true;email.autocomplete='email';email.setAttribute('aria-label','Email address');email.setAttribute('aria-describedby','waitlist-errors');const label=email.closest('.ml-field-group')?.querySelector('label');if(label)label.htmlFor=email.id;
    email.addEventListener('invalid',()=>{errors.textContent='Enter a valid email address to join the waitlist.';email.setAttribute('aria-invalid','true')});
    email.addEventListener('input',()=>{email.removeAttribute('aria-invalid');errors.textContent=''});
   }
   target.querySelector('form')?.addEventListener('submit',event=>{if(consent&&!consent.checked){event.preventDefault();event.stopImmediatePropagation();errors.textContent='Please select the checkbox to agree to PlayCall launch and beta-opportunity emails.';consent.focus()}else{errors.textContent=''}},true);
   observer.disconnect()}
 });observer.observe(target,{childList:true,subtree:true});
 setTimeout(()=>{if(!button.hidden){status.textContent='The embedded form has not loaded. You can use the MailerLite form link below instead. No signup has been completed here.';observer.disconnect()}},15000);
});
