
from re import search
from modloader import modast, modinfo
from modloader.modclass import Mod, loadable_mod
import jz_magmalink as ml

@loadable_mod
class AWSWMod(Mod):
    name = "A Day at the Park"
    version = "0.0"
    author = "Ryann1706"
    dependencies = ["MagmaLink"]

    def mod_load(self):
        pass

    def mod_complete(self):
        pass


    # Replacing Vara's sprite with the small one in the chaper 4 investigation
    ml.find_label("c4hatchery") \
        .search_if("adinestatus == \"bad\"").branch_else() \
        .search_if("remystatus == \"bad\"").branch("remygoodending == True") \
        .search_say("I'm glad we did. It was long overdue.") \
        .hook_to("ryann_adatp_vara_fix_adine") 

    ml.find_label("c4hatchery") \
        .search_if("adinestatus == \"bad\"").branch_else() \
        .search_if("remystatus == \"bad\"").branch("remygoodending == True") \
        .search_say("Vara, do you know who that is? Hmm?") \
        .link_from("ryann_adatp_vara_adine_return")
        
    ml.find_label("c4hatchery") \
        .search_if("adinestatus == \"bad\"").branch_else() \
        .search_if("remystatus == \"bad\"").branch("persistent.remygoodending == True") \
        .search_say("Good job, [player_name].") \
        .hook_to("ryann_adatp_vara_fix_adine2") 

    ml.find_label("c4hatchery") \
        .search_if("adinestatus == \"bad\"").branch_else() \
        .search_if("remystatus == \"bad\"").branch("persistent.remygoodending == True") \
        .search_say("Vara, do you know who that is? Hmm?") \
        .link_from("ryann_adatp_vara_adine_return2")

    ml.find_label("c4hatchery") \
        .search_if("adinestatus == \"bad\"").branch("adinestatus == \"none\"") \
        .search_if("remystatus == \"bad\"").branch("remygoodending == True") \
        .search_say("I'm glad we did. It was long overdue.") \
        .hook_to("ryann_adatp_vara_fix_remy")

    ml.find_label("c4hatchery") \
        .search_if("adinestatus == \"bad\"").branch("adinestatus == \"none\"") \
        .search_if("remystatus == \"bad\"").branch("remygoodending == True") \
        .search_say("Vara, do you know who that is? Hmm?") \
        .link_from("ryann_adatp_vara_remy_return")

    ml.find_label("c4hatchery") \
        .search_if("adinestatus == \"bad\"").branch("adinestatus == \"none\"") \
        .search_if("remystatus == \"bad\"").branch("persistent.remygoodending == True") \
        .search_say("Good job, [player_name].") \
        .hook_to("ryann_adatp_vara_fix_remy2")

    ml.find_label("c4hatchery") \
        .search_if("adinestatus == \"bad\"").branch("adinestatus == \"none\"") \
        .search_if("remystatus == \"bad\"").branch("persistent.remygoodending == True") \
        .search_say("Vara, do you know who that is? Hmm?") \
        .link_from("ryann_adatp_vara_remy_return2")


    # Delivering the PDA with Remy having three scenes done
    ml.find_label("c4library") \
        .search_if("remystatus == \"good\"").branch() \
        .search_say("I may not be working today, but I'm still going to check it out as soon as possible.") \
        .hook_to("ryann_adatp_start_pda", condition="remyscenesfinished == 3" and "c4sectionsplayed == 1")

    # Delivering the PDA with Remy having three scenes done
    ml.find_label("c4library") \
        .search_if("remystatus == \"good\"").branch("remystatus == \"neutral\"") \
        .search_say("I may not be working today, but I'm still going to check it out as soon as possible.") \
        .hook_to("ryann_adatp_start_pda2", condition="remyscenesfinished == 3" and "c4sectionsplayed == 1")

    # Going to the orphanage with Remy having three scenes done
    ml.find_label("c4hatchery") \
        .search_if("adinestatus == \"bad\"").branch("adinestatus == \"none\"") \
        .search_if("remystatus == \"bad\"").branch("remygoodending == True") \
        .search_say("Yeah, probably.") \
        .hook_to("ryann_adatp_start_orphanage_remy", condition="remyscenesfinished == 3" and "c4sectionsplayed == 1") 

    # Going to the orphanage with Remy having three scenes done
    ml.find_label("c4hatchery") \
        .search_if("adinestatus == \"bad\"").branch("adinestatus == \"none\"") \
        .search_if("remystatus == \"bad\"").branch("persistent.remygoodending == True") \
        .search_say("Yeah, probably.") \
        .hook_to("ryann_adatp_start_orphanage_remy2", condition="remyscenesfinished == 3" and "c4sectionsplayed == 1")
        
    # Going to the orphanage with Adine having three scenes done
    ml.find_label("c4hatchery") \
        .search_if("adinestatus == \"bad\"").branch_else() \
        .search_if("remystatus == \"bad\"").branch("remygoodending == True") \
        .search_say("She's definitely listening, though. Isn't that right?") \
        .hook_to("ryann_adatp_start_orphanage_adine", condition="adinescenesfinished == 3" and "c4sectionsplayed == 1")

    # Going to the orphanage with Adine having three scenes done
    ml.find_label("c4hatchery") \
        .search_if("adinestatus == \"bad\"").branch_else() \
        .search_if("remystatus == \"bad\"").branch("persistent.remygoodending == True") \
        .search_say("She doesn't talk much.") \
        .hook_to("ryann_adatp_start_orphanage_adine2", condition="adinescenesfinished == 3" and "c4sectionsplayed == 1")
        
    
