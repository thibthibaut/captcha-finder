from bs4 import BeautifulSoup



data = '''
<!DOCTYPE html>

<html lang="fr">

<head>
    <meta charset="UTF-8" />
    				<meta http-equiv="X-UA-Compatible" content="IE=edge">
			<link rel="stylesheet" href="/bundles/ripconsultation/css/ui-lightness/jquery-ui-1.10.4.custom.css" type="text/css" media="all" />
                        	<link rel="stylesheet" href="/css/c62f8bf.css" type="text/css" media="all" />
                          <link rel="stylesheet" href="/bundles/ripconsultation/css/print.css" type="text/css" media="print" />
            
	
    <meta name="viewport" content="width=device-width, initial-scale=1.0">

    
<!--[if lt IE 9]>
    	<script src="/js/cba3e51.js"></script>
  <![endif]-->
    <script type="text/javascript" src="/ruxitagentjs_ICA27SVfjqrx_10167190521165248.js" data-dtconfig="rid=RID_1780581884|rpid=-555447334|domain=interieur.gouv.fr|reportUrl=/rb_984604b4-2542-4bdb-9477-2bedd99aebb9|app=7b801f37abff0e14|featureHash=ICA27SVfjqrx|srsr=25000|rdnt=1|uxrgce=1|bp=2|srms=1,1,,,|uxrgcm=100,25,300,3;100,25,300,3|dpvc=1|lastModification=1561540512680|dtVersion=10167190521165248|tp=500,50,0,1|uxdcw=1500|agentUri=/ruxitagentjs_ICA27SVfjqrx_10167190521165248.js"></script><script src="/js/e163ef0.js"></script>

<script>
$(function () {
  var nua = navigator.userAgent
  var isAndroid = (nua.indexOf('Mozilla/5.0') > -1 && nua.indexOf('Android ') > -1 && nua.indexOf('AppleWebKit') > -1 && nua.indexOf('Chrome') === -1)
  if (isAndroid) {
    $('select.form-control').removeClass('form-control').css('width', '100%')
  }
})
</script>


     


    <title>	Référendum d'initiative partagée

</title>
    <link rel="shortcut icon" href="/favicon.ico" />        </head>

<body>


        <!-- No navbar included here to reduce dependencies, see https://github.com/phiamo/MopaBootstrapSandboxBundle/blob/master/Resources/views/base.html.twig for howto include it -->
    
    <header role="banner">
    <div class="container">
 		<div id="entete" class="row">
			<div class="col-xs-12 col-sm-3">
			     <p class="logo-rf" alt="Logo République Française" />
			</div>
		    			<div class="col-xs-12 col-sm-9">
				<h1 class="titre">Référendum d'initiative partagée</h1>
			</div>
					</div> <!-- fin row entete -->
    </div> <!-- fin container -->
</header> <!-- fin entete -->

<nav role="navigation">
    <div class="container">
        <div class=""> <!-- class page-header retirée -->
            <div class="row">
                <div class="">
                                            <div class="subnav ">
                                                                            <ul class="nav nav-pills">
            
                <li class="first">        <a href="/">
Accueil</a>        
    </li>

    
                <li>        <a href="/contenu/comment-ca-marche">
En savoir plus sur le RIP</a>        
    </li>

    
                <li>        <a href="/contenu/initiatives">
Déposer un soutien</a>        
    </li>

    
                <li>        <a href="/contenu/consultations">
Consultation des soutiens déposés</a>        
    </li>

    
                <li>        <a href="/contenu/reclamations">
Réclamations</a>        
    </li>

    
                <li>        <a href="/contenu/recours">
Recours</a>        
    </li>

    
                <li>        <a href="https://www.interieur.gouv.fr/RIP/Referendum-d-initiative-partagee-le-tutoriel" target="_blank">
Tutoriel</a>        
    </li>

    
                <li class="last">        <a href="https://www.interieur.gouv.fr/RIP/Referendum-d-initiative-partagee-foire-aux-questions" target="_blank">
FAQ</a>        
    </li>


    </ul>

                            </div>
                                    </div>
            </div>
        </div>
    </div>
</nav>

<main role="main">
    <div class="container">
        <div class="row">
            <div class="" id="contenu">
                
<div class="row-fluid" style="margin-top: 10px;">
    <div class="col-xs-12 col-sm-12">
        <div id="formulaire_consultation_publique">

                            <div class="row well">
	    Proposition de loi référendaire : Proposition de loi visant à affirmer le caractère de service public national de l&#039;exploitation des aérodromes de Paris
</div>
            
                            <div class="row well alphabet">
	    	    	                    
    	    	     	
						    	
			        	<a style="" href="/consultation_publique/8/A"  >A</a>
		    	     	
										        	<a style="color:red" href="/consultation_publique/8/B"  >B</a>
		    	     	
						    	
			        	<a style="" href="/consultation_publique/8/C"  >C</a>
		    	     	
						    	
			        	<a style="" href="/consultation_publique/8/D"  >D</a>
		    	     	
						    	
			        	<a style="" href="/consultation_publique/8/E"  >E</a>
		    	     	
						    	
			        	<a style="" href="/consultation_publique/8/F"  >F</a>
		    	     	
						    	
			        	<a style="" href="/consultation_publique/8/G"  >G</a>
		    	     	
						    	
			        	<a style="" href="/consultation_publique/8/H"  >H</a>
		    	     	
						    	
			        	<a style="" href="/consultation_publique/8/I"  >I</a>
		    	     	
						    	
			        	<a style="" href="/consultation_publique/8/J"  >J</a>
		    	     	
						    	
			        	<a style="" href="/consultation_publique/8/K"  >K</a>
		    	     	
						    	
			        	<a style="" href="/consultation_publique/8/L"  >L</a>
		    	     	
						    	
			        	<a style="" href="/consultation_publique/8/M"  >M</a>
		    	     	
						    	
			        	<a style="" href="/consultation_publique/8/N"  >N</a>
		    	     	
						    	
			        	<a style="" href="/consultation_publique/8/O"  >O</a>
		    	     	
						    	
			        	<a style="" href="/consultation_publique/8/P"  >P</a>
		    	     	
						    	
			        	<a style="" href="/consultation_publique/8/Q"  >Q</a>
		    	     	
						    	
			        	<a style="" href="/consultation_publique/8/R"  >R</a>
		    	     	
						    	
			        	<a style="" href="/consultation_publique/8/S"  >S</a>
		    	     	
						    	
			        	<a style="" href="/consultation_publique/8/T"  >T</a>
		    	     	
						    	
			        	<a style="" href="/consultation_publique/8/U"  >U</a>
		    	     	
						    	
			        	<a style="" href="/consultation_publique/8/V"  >V</a>
		    	     	
						    	
			        	<a style="" href="/consultation_publique/8/W"  >W</a>
		    	     	
						    	
			        	<a style="" href="/consultation_publique/8/X"  >X</a>
		    	     	
						    	
			        	<a style="" href="/consultation_publique/8/Y"  >Y</a>
		    	     	
						    	
			        	<a style="" href="/consultation_publique/8/Z"  >Z</a>
		</div>
<div class="row well alphabet">

    							    	
			        	<a style="" href="/consultation_publique/8/B/BA"  >BA</a>
												        	<a style="color:red" href="/consultation_publique/8/B/BB"  >BB</a>
								    	
			        	<a style="" href="/consultation_publique/8/B/BC"  >BC</a>
								    	
			        	<a style="" href="/consultation_publique/8/B/BD"  >BD</a>
								    	
			        	<a style="" href="/consultation_publique/8/B/BE"  >BE</a>
								    	
			        	<a style="" href="/consultation_publique/8/B/BF"  >BF</a>
								    	
			        	<a style="" href="/consultation_publique/8/B/BG"  >BG</a>
								    	
			        	<a style="" href="/consultation_publique/8/B/BH"  >BH</a>
								    	
			        	<a style="" href="/consultation_publique/8/B/BI"  >BI</a>
								    	
			        	<a style="" href="/consultation_publique/8/B/BJ"  >BJ</a>
								    	
			        	<a style="" href="/consultation_publique/8/B/BK"  >BK</a>
								    	
			        	<a style="" href="/consultation_publique/8/B/BL"  >BL</a>
								    	
			        	<a style="" href="/consultation_publique/8/B/BM"  >BM</a>
								    	
			        	<a style="" href="/consultation_publique/8/B/BN"  >BN</a>
								    	
			        	<a style="" href="/consultation_publique/8/B/BO"  >BO</a>
								    	
			        	<a style="" href="/consultation_publique/8/B/BP"  >BP</a>
								    	
			        	<a style="" href="/consultation_publique/8/B/BQ"  >BQ</a>
								    	
			        	<a style="" href="/consultation_publique/8/B/BR"  >BR</a>
								    	
			        	<a style="" href="/consultation_publique/8/B/BS"  >BS</a>
								    	
			        	<a style="" href="/consultation_publique/8/B/BT"  >BT</a>
								    	
			        	<a style="" href="/consultation_publique/8/B/BU"  >BU</a>
								    	
			        	<a style="" href="/consultation_publique/8/B/BV"  >BV</a>
								    	
			        	<a style="" href="/consultation_publique/8/B/BW"  >BW</a>
								    	
			        	<a style="" href="/consultation_publique/8/B/BX"  >BX</a>
								    	
			        	<a style="" href="/consultation_publique/8/B/BY"  >BY</a>
								    	
			        	<a style="" href="/consultation_publique/8/B/BZ"  >BZ</a>
		</div>
            
                                                <div class="row well">
	    	
		<div class="row well">
				<div class="col-md-12 text-center">
				</div>
		</div>
        
</div>
<div class="row-fluid">
	<div class="col-md-12 text-center">
		 <a class="btn btn-default"  href="/consultation_publique">Retour</a>
	</div>
</div>                                    </div>

        <div class="well dark-well">
            <p>Rappel - la loi n° 2013-1116 du 6 décembre 2013 prévoit les sanctions suivantes en cas de fraudes intervenant dans le cadre du dépôt des soutiens aux propositions de loi référendaire ainsi qu'en cas d'utilisation frauduleuse des données déposées :
            </p>
            <p>Art. L. 558-38 du code électoral - Le fait, pour toute personne participant aux opérations de recueil des soutiens à une proposition de loi présentée au titre de l'article 11 de la Constitution, d'usurper l'identité d'un électeur inscrit sur la liste électorale ou de tenter de commettre cette usurpation est puni de deux ans d'emprisonnement et 30 000 € d'amende.
            </p>
            <p>Art. L. 558-39 du code électoral - Le fait, dans le cadre des mêmes opérations, de soustraire ou d'altérer, de manière frauduleuse, les données collectées ou de tenter de commettre cette soustraction, cet ajout ou cette altération est puni de cinq ans d'emprisonnement et 75 000 € d'amende.
            </p>
            <p>Les peines sont portées à sept ans d'emprisonnement et 100 000 € d'amende lorsque les faits mentionnés au premier alinéa sont commis avec violence.
            </p>
            <p>Art. L. 558-40 du code électoral - Le fait, dans le cadre des mêmes opérations, de déterminer ou tenter de déterminer un électeur à apporter son soutien ou à s'en abstenir à l'aide de menaces, violences, contraintes, abus d'autorité ou abus de pouvoir est puni de deux ans d'emprisonnement et 15 000 € d'amende.
            </p><p>Art. L. 558-41 du code électoral - Le fait, dans le cadre des mêmes opérations, de proposer, directement ou indirectement, des offres, des promesses, des dons, des présents ou des avantages quelconques afin de déterminer l'électeur à apporter son soutien ou à s'en abstenir est puni de deux ans d'emprisonnement et 15 000 € d'amende. Le fait d'agréer ou de solliciter ces mêmes offres, promesses, dons, présents ou avantages quelconques est puni des mêmes peines.
            </p>
            <p>Art. L. 558-42 du code électoral - Le fait, dans le cadre des mêmes opérations, de reproduire des données collectées à d'autres fins que celles de vérification et de contrôle ou de tenter de commettre cette reproduction est puni de cinq ans d'emprisonnement et de 75 000 € d'amende.
            </p>
            <p>Art. L. 558-43 du code électoral - Les personnes coupables de l'une des infractions prévues au présent chapitre peuvent être également condamnées à :
            <ul>
                <li> L'interdiction des droits civiques suivant les modalités prévues aux 1° et 2° de l'article 131-26 du code pénal ;</li>
                <li> L'affichage ou la diffusion de la décision mentionnés à l'article 131-35 et au 9° de l'article 131-39 du même code.</li>
            </ul>
            </p>
        </div>

    </div>

</div>
   
            </div>
        </div>    
    </div>
</main>


    <footer role="contentinfo">
        <div class="container">
                        <div id="pied" class="row">
				<div class="col-sm-12 col-lg-4">Rip Web Citoyen  - 2.4.6</div>
    			<div id="link-documents" class="col-sm-12 col-lg-4">| <a class="footer-link" href="/contenu/mentions-legales">Mentions Légales</a> |</div>
    			<div id="copyright" class="col-sm-12 col-lg-4">Tous droits réservés &copy; Ministère de l'intérieur</div>
    	    </div>
                    </div>
    </footer>

     
          

        
                
    <script type="text/javascript">
        $(document).ready(function () {
            $('[data-toggle="tooltip"]').tooltip();
            $('[data-toggle="popover"]').popover();
        });
    </script>
    
</body>
</html>
'''



html = BeautifulSoup(data, 'html.parser')


mess = html.find('h2')

if mess != None:
    if 'Aucun soutien' in mess.text:
        print('AUCUN SOUTIEN DETECTE')


