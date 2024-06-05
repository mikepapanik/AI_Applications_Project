import numpy
import imageio
import genetic
import pygad
import matplotlib.pyplot

# Ανάγνωση εικόνας στόχου για αναπαραγωγή με χρήση γενετικού αλγορίθμου (GA).
target_im = imageio.imread('acropolis.jpg')
target_im = numpy.asarray(target_im/255, dtype=numpy.float)

# Στόχευση εικόνας μετά την κωδικοποίηση. Χρησιμοποιείται κωδικοποίηση αξίας.
target_chromosome = genetic.img2chromosome(target_im)

def fitness_fun(solution, solution_idx):
    """
    Υπολογισμός της τιμής καταλληλότητας για μια λύση στον πληθυσμό.
     Η τιμή καταλληλότητας υπολογίζεται χρησιμοποιώντας το άθροισμα της απόλυτης διαφοράς μεταξύ 
     των τιμών των γονιδίων στα αρχικά και τα αναπαραγόμενα χρωμοσώματα.
    Λύση: Η τρέχουσα λύση στον πληθυσμό για τον υπολογισμό της καταλληλότητάς του.
     solution_idx: Ευρετήριο της λύσης εντός του πληθυσμού.
    """

    fitness = numpy.sum(numpy.abs(target_chromosome-solution))

    # Αρνείται την αξία της φυσικής κατάστασης ώστε να αυξάνεται και όχι να μειώνεται.
    fitness = numpy.sum(target_chromosome) - fitness
    return fitness

def callback(ga_instance):
    print("Generation = {gen}".format(gen=ga_instance.generations_completed))
    print("Fitness    = {fitness}".format(fitness=ga_instance.best_solution()[1]))

    if ga_instance.generations_completed % 500 == 0:
        matplotlib.pyplot.imsave('solution_'+str(ga_instance.generations_completed)+'.png', genetic.chromosome2img(ga_instance.best_solution()[0], target_im.shape))

ga_instance = pygad.GA(num_generations=20000,
                       num_parents_mating=10,
                       fitness_func=fitness_fun,
                       sol_per_pop=20,
                       num_genes=target_im.size,
                       init_range_low=0.0,
                       init_range_high=1.0,
                       mutation_percent_genes=0.01,
                       mutation_type="random",
                       mutation_by_replacement=True,
                       random_mutation_min_val=0.0,
                       random_mutation_max_val=1.0,
                       callback_generation=callback)

ga_instance.run()

# Μετά την ολοκλήρωση των γενεών, εμφανίζονται ορισμένες περιγραφές που συνοψίζουν τον τρόπο 
#με τον οποίο εξελίσσονται οι τιμές των αποτελεσμάτων/φυσικής κατάστασης με τις γενιές.
ga_instance.plot_result()

# Επιστρέφοντας τις λεπτομέρειες της καλύτερης λύσης.
solution, solution_fitness, solution_idx = ga_instance.best_solution()
print("Fitness value of the best solution = {solution_fitness}".format(solution_fitness=solution_fitness))
print("Index of the best solution : {solution_idx}".format(solution_idx=solution_idx))

if ga_instance.best_solution_generation != -1:
    print("Best fitness value reached after {best_solution_generation} generations.".format(best_solution_generation=ga_instance.best_solution_generation))

result = genetic.chromosome2img(solution, target_im.shape)
matplotlib.pyplot.imshow(result)
matplotlib.pyplot.title("MPPL20059_MPPL20067")
matplotlib.pyplot.show()