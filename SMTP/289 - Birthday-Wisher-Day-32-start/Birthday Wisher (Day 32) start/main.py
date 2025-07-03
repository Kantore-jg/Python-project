from email.message import EmailMessage
import ssl
import smtplib

email_sender ='kantorejeangildas@gmail.com'
pwd = 'mljk yikz abrv daan'
email_receiver = [
    "abayo.gisele@eseaybank.bi",
    "nshimirimana.kevin@ub.edu.bi",
    "mukamana.anne@demo.bi",
    "kabura.fatma@post.bi",
    "nkengurutse.leonce@bi-finance.bi",
    "mugisha.audrey@test.bi",
    "nyandwi.richard@bujumail.bi",
    "habonimana.sandrine@demo.bi",
    "ninahazwe.jean@eseaybank.bi",
    "habimana.esther@ub.edu.bi",
    "client01@eseaybank.bi",
    "client02@eseaybank.bi",
    "client03@eseaybank.bi",
    "client04@eseaybank.bi",
    "client05@eseaybank.bi",
    "alice.karenzo@ub.edu.bi",
    "diane.niyonsaba@demo.bi",
    "emmanuel.nkurunziza@bi-smart.bi",
    "florence.nyandwi@eseaybank.bi",
    "grace.irimina@bujumail.bi",
    "henri.mukiza@ub.edu.bi",
    "ingabire.melissa@post.bi",
    "jack.mugiraneza@test.bi",
    "keza.joelle@eseaybank.bi",
    "leonidas.ndayiragije@bujubank.bi",
    "maria.bisimwa@ub.edu.bi",
    "nadine.kazuba@demo.bi",
    "olivier.rugema@smartmail.bi",
    "pauline.mutoni@eseaybank.bi",
    "quentin.ndikumana@bujumail.bi",
    "rachel.niyungeko@ub.edu.bi",
    "samuel.kanyange@demo.bi",
    "theodore.bizimana@eseaybank.bi",
    "ursule.nshimiye@ub.edu.bi",
    "victor.nkurunziza@test.bi",
    "wanda.irakoze@bujumail.bi",
    "yvan.ndikumana@post.bi",
    "zita.burundiana@eseaybank.bi",
    "agnes.kabura@ub.edu.bi",
    "benoit.niyongabo@demo.bi",
    "clarisse.ndihokubwayo@smartmail.bi",
    "denis.irambona@ub.edu.bi",
    "edith.mutima@eseaybank.bi",
    "franck.kazungu@bujumail.bi",
    "gloria.nyabenda@ub.edu.bi",
    "herve.nsanze@post.bi",
    "isabelle.kanyana@eseaybank.bi",
    "jeanluc.irakoze@demo.bi",
    "karine.nkundwa@test.bi",
    "lionel.niyonsenga@bujubank.bi",
    "marieclaire.mugiraneza@ub.edu.bi",
    "nadege.bukene@demo.bi",
    "oscar.ndikumana@post.bi",
    "prisca.iradukunda@eseaybank.bi",
    "quincy.ndayikengurukiye@ub.edu.bi",
    "rolande.mukeshimana@test.bi",
    "steve.mugisha@demo.bi",
    "tania.nshimiyimana@bujumail.bi",
    "ulrick.ndikuriyo@ub.edu.bi",
    "viviane.kazungu@eseaybank.bi",
    "willy.munyakazi@demo.bi",
    "xavier.bujumbura@test.bi",
    "yasmina.ndikumana@smartmail.bi",
    "zacharie.niyubahwe@post.bi",
    "alpha.nsanze@eseaybank.bi",
    "brigitte.karirekinyana@ub.edu.bi",
    "cedric.niyongabo@test.bi",
    "david.irakoze@demo.bi",
    "eline.mugisha@bujubank.bi",
    "fabien.nduwimana@ub.edu.bi",
    "gina.burundienne@post.bi",
    "hubert.mugiraneza@eseaybank.bi",
    "irene.niyongere@demo.bi",
    "joseph.ndikumana@ub.edu.bi",
    "karine.ndayishimiye@demo.bi",
    "laurent.nkurunziza@post.bi",
    "murielle.irakoze@smartmail.bi",
    "nicolas.ndikumana@ub.edu.bi",
    "odette.kanyana@eseaybank.bi",
    "philippe.nibigira@test.bi",
    "queen.niyongere@ub.edu.bi",
    "ramadhan.kazungu@demo.bi",
    "solange.mukamana@eseaybank.bi",
    "thibault.burundi@ub.edu.bi",
    "ursuline.ndikuriyo@test.bi",
    "vianney.irambona@bujumail.bi",
    "wilfried.niyonkuru@ub.edu.bi",
    "xena.kazuba@demo.bi",
    "yves.ndabirabe@post.bi",
    "zoe.karirekinyana@eseaybank.bi",
    "andre.ndikumanayo@ub.edu.bi",
    "bella.kazungu@test.bi",
    "celestin.iradukunda@demo.bi",
    "danielle.munyaneza@bujubank.bi",
    "elias.ndikumana@ub.edu.bi",
    "fanny.burundi@post.bi",
    "gaspard.niyongere@eseaybank.bi",
    "huguette.mugiraneza@demo.bi",
    "ivan.nkurunziza@ub.edu.bi",
    "josiane.niyongabo@test.bi",
    "kassy.irakoze@bujumail.bi",
    "leo.ndayishimiye@demo.bi",
    "manu.mugiraneza@smartmail.bi",
    "nelly.kazungu@eseaybank.bi"
]

#email_receiver='francis.mcdanzo@gmail.com'


subject = "check out my new video"

body = ''''
and here is the link : https://www.youtube.com/watch?v=aBi-g1giKOs&list=RDaBi-g1giKOs&start_radio=1

just pull up
'''

em = EmailMessage()
em['From'] = email_sender
em['To']= ','.join(email_receiver)
em['Subject'] = subject
em.set_content(body)
context = ssl.create_default_context()

with smtplib.SMTP_SSL('smtp.gmail.com',465,context=context) as smtp:
    smtp.login(email_sender,pwd)
    smtp.sendmail(email_sender,email_receiver,em.as_string())



