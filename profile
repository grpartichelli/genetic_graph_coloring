 Score: 102291.34 | Num Colors: 12 | Generations: 35
         9531710 function calls (9531674 primitive calls) in 5.213 seconds

   Ordered by: internal time

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
   232005    1.206    0.000    1.675    0.000 coloring.py:70(addRestriction)
   222005    1.040    0.000    1.499    0.000 coloring.py:76(removeRestriction)
  3206272    0.469    0.000    0.469    0.000 {method 'add' of 'set' objects}
  3068352    0.460    0.000    0.460    0.000 {method 'discard' of 'set' objects}
    99961    0.265    0.000    0.265    0.000 coloring.py:201(findLeastWeightColorNotUsedByNeighbors)
    59500    0.207    0.000    0.352    0.000 coloring.py:236(findRandomAvailableColor)
   222005    0.201    0.000    1.700    0.000 coloring.py:85(uncolorVertice)
   232005    0.191    0.000    1.865    0.000 coloring.py:95(colorVertice)
   222005    0.142    0.000    3.626    0.000 coloring.py:81(swapColors)
   195051    0.126    0.000    0.182    0.000 random.py:238(_randbelow_with_getrandbits)
      720    0.124    0.000    0.156    0.000 coloring.py:5(__init__)
      146    0.117    0.001    1.685    0.012 genetic.py:104(mutateBest)
   135561    0.113    0.000    0.237    0.000 random.py:291(randrange)
      119    0.080    0.001    1.599    0.013 genetic.py:91(mutateRandom)
   793788    0.080    0.000    0.080    0.000 {method 'append' of 'list' objects}
   135561    0.063    0.000    0.300    0.000 random.py:335(randint)
      271    0.062    0.000    1.411    0.005 genetic.py:126(crossover)
      100    0.058    0.001    0.063    0.001 graph.py:62(bfs)
    59490    0.038    0.000    0.105    0.000 random.py:344(choice)
   230381    0.030    0.000    0.030    0.000 {method 'getrandbits' of '_random.Random' objects}
   195051    0.027    0.000    0.027    0.000 {method 'bit_length' of 'int' objects}
    91300    0.021    0.000    0.021    0.000 coloring.py:171(isValid)
       20    0.021    0.001    0.307    0.015 coloring.py:114(colorGreedy)
    86902    0.011    0.000    0.011    0.000 {built-in method builtins.len}
      100    0.009    0.000    0.072    0.001 graph.py:31(get_separated_graph)
    10062    0.008    0.000    0.008    0.000 coloring.py:188(findSmallestColorNotUsedByNeighbors)
        1    0.007    0.007    5.125    5.125 genetic.py:8(geneticSolve)
    12990    0.005    0.000    0.008    0.000 graph.py:7(__lt__)
        1    0.005    0.005    0.007    0.007 input.py:75(__init__)
      700    0.004    0.000    0.156    0.000 coloring.py:21(__copy__)
        1    0.003    0.003    0.004    0.004 graph.py:14(__init__)
       55    0.003    0.000    0.012    0.000 {method 'sort' of 'list' objects}
      525    0.003    0.000    0.010    0.000 genetic.py:186(tournamentSelection)
        8    0.002    0.000    0.066    0.008 coloring.py:142(fixColors)
      700    0.002    0.000    0.158    0.000 copy.py:66(copy)
     1315    0.001    0.000    0.002    0.000 random.py:504(uniform)
     3451    0.001    0.000    0.001    0.000 {method 'split' of 'str' objects}
      525    0.001    0.000    0.001    0.000 genetic.py:178(getNumCompetitors)
      741    0.001    0.000    0.001    0.000 coloring.py:51(getScore)
        4    0.001    0.000    0.001    0.000 {built-in method _imp.create_dynamic}
      734    0.000    0.000    0.000    0.000 {built-in method builtins.max}
     3451    0.000    0.000    0.000    0.000 {method 'strip' of 'str' objects}
        1    0.000    0.000    5.209    5.209 main.py:11(main)
      525    0.000    0.000    0.010    0.000 genetic.py:160(selectParents)
     1315    0.000    0.000    0.000    0.000 {method 'random' of '_random.Random' objects}
      760    0.000    0.000    0.000    0.000 {built-in method builtins.getattr}
      700    0.000    0.000    0.001    0.000 genetic.py:229(<lambda>)
        6    0.000    0.000    0.000    0.000 {built-in method marshal.loads}
      700    0.000    0.000    0.000    0.000 {built-in method builtins.issubclass}
       26    0.000    0.000    0.001    0.000 <frozen importlib._bootstrap_external>:1438(find_spec)
        1    0.000    0.000    5.213    5.213 main.py:1(<module>)
      500    0.000    0.000    0.000    0.000 graph.py:3(__init__)
      720    0.000    0.000    0.000    0.000 {method 'get' of 'dict' objects}
      251    0.000    0.000    0.000    0.000 coloring.py:104(createNewColor)
      265    0.000    0.000    0.000    0.000 genetic.py:80(getNumMutations)
       42    0.000    0.000    0.000    0.000 {built-in method posix.stat}
        8    0.000    0.000    0.000    0.000 {built-in method io.open_code}
        6    0.000    0.000    0.000    0.000 {built-in method builtins.__build_class__}
        1    0.000    0.000    0.311    0.311 genetic.py:218(getStartingPopulation)
      120    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:62(_path_join)
      120    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:64(<listcomp>)
        8    0.000    0.000    0.000    0.000 {method 'read' of '_io.BufferedReader' objects}
        6    0.000    0.000    0.001    0.000 <frozen importlib._bootstrap_external>:856(get_code)
       10    0.000    0.000    0.001    0.000 <frozen importlib._bootstrap>:901(_find_spec)
       10    0.000    0.000    0.001    0.000 <frozen importlib._bootstrap_external>:1309(_get_spec)
       35    0.000    0.000    0.002    0.000 genetic.py:228(orderPopulationByScore)
        1    0.000    0.000    0.002    0.002 random.py:1(<module>)
     10/4    0.000    0.000    0.003    0.001 <frozen importlib._bootstrap>:1002(_find_and_load)
       37    0.000    0.000    0.000    0.000 {built-in method time.time}
       10    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:486(_init_module_attrs)
       12    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:301(cache_from_source)
     10/4    0.000    0.000    0.003    0.001 <frozen importlib._bootstrap>:659(_load_unlocked)
       10    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:166(_get_module_lock)
      138    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:231(_verbose_message)
       36    0.000    0.000    0.000    0.000 genetic.py:203(shouldKeepGoing)
        2    0.000    0.000    0.000    0.000 {function Random.seed at 0x7f39106509d0}
        2    0.000    0.000    0.000    0.000 {built-in method _imp.source_hash}
      132    0.000    0.000    0.000    0.000 {method 'join' of 'str' objects}
      252    0.000    0.000    0.000    0.000 {method 'rstrip' of 'str' objects}
       10    0.000    0.000    0.000    0.000 {built-in method posix.getcwd}
        8    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:976(get_data)
        8    0.000    0.000    0.000    0.000 {method '__exit__' of '_io._IOBase' objects}
       10    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:636(spec_from_file_location)
       10    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:87(acquire)
     10/4    0.000    0.000    0.003    0.001 <frozen importlib._bootstrap>:967(_find_and_load_unlocked)
        1    0.000    0.000    0.000    0.000 {built-in method io.open}
       10    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:112(release)
       32    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:1272(_path_importer_cache)
       10    0.000    0.000    0.001    0.000 <frozen importlib._bootstrap>:558(module_from_spec)
       42    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:80(_path_stat)
      7/1    0.000    0.000    5.213    5.213 {built-in method builtins.exec}
        7    0.000    0.000    0.000    0.000 coloring.py:60(calculatePunishment)
        6    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:585(_compile_bytecode)
      6/4    0.000    0.000    0.003    0.001 <frozen importlib._bootstrap_external>:784(exec_module)
       16    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:385(cached)
       10    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:1433(_get_spec)
       70    0.000    0.000    0.000    0.000 {method 'rpartition' of 'str' objects}
        6    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:500(_classify_pyc)
       10    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:431(_get_cached)
        2    0.000    0.000    0.000    0.000 random.py:126(seed)
       10    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:58(__init__)
        4    0.000    0.000    0.001    0.000 <frozen importlib._bootstrap_external>:1106(create_module)
       10    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:185(cb)
       14    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:51(_unpack_uint32)
       47    0.000    0.000    0.000    0.000 {built-in method builtins.hasattr}
     14/4    0.000    0.000    0.002    0.001 <frozen importlib._bootstrap>:220(_call_with_frames_removed)
       10    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:156(__enter__)
        5    0.000    0.000    0.000    0.000 codecs.py:319(decode)
       10    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:398(parent)
       30    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:878(__exit__)
        1    0.000    0.000    0.000    0.000 {built-in method builtins.round}
        1    0.000    0.000    0.000    0.000 coloring.py:270(small_print)
       10    0.000    0.000    0.001    0.000 <frozen importlib._bootstrap_external>:1341(find_spec)
       12    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:68(_path_split)
        1    0.000    0.000    0.000    0.000 genetic.py:1(<module>)
       50    0.000    0.000    0.000    0.000 {built-in method builtins.isinstance}
       30    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:874(__enter__)
        1    0.000    0.000    0.000    0.000 random.py:101(Random)
        2    0.000    0.000    0.000    0.000 {built-in method builtins.print}
       10    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:90(_path_is_mode_type)
       14    0.000    0.000    0.000    0.000 {method 'endswith' of 'str' objects}
       50    0.000    0.000    0.000    0.000 {built-in method _imp.acquire_lock}
       10    0.000    0.000    0.000    0.000 {built-in method _imp.is_builtin}
       10    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:351(__init__)
       50    0.000    0.000    0.000    0.000 {built-in method _imp.release_lock}
        5    0.000    0.000    0.000    0.000 {built-in method _codecs.utf_8_decode}
        6    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:463(_check_name_wrapper)
       10    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:99(_path_isfile)
        1    0.000    0.000    0.000    0.000 bisect.py:1(<module>)
       10    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:160(__exit__)
        4    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:1114(exec_module)
       10    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:736(find_spec)
        6    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:1017(path_stats)
        1    0.000    0.000    0.000    0.000 {method 'close' of '_io.TextIOWrapper' objects}
        1    0.000    0.000    0.000    0.000 coloring.py:4(Coloring)
        6    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:35(_new_module)
        4    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:533(_validate_timestamp_pyc)
        1    0.000    0.000    0.000    0.000 input.py:4(getTerminalInput)
       10    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:152(__init__)
        1    0.000    0.000    0.000    0.000 {built-in method math.exp}
        1    0.000    0.000    0.000    0.000 coloring.py:1(<module>)
       10    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:811(find_spec)
       20    0.000    0.000    0.000    0.000 {built-in method _thread.allocate_lock}
       20    0.000    0.000    0.000    0.000 {method '__exit__' of '_thread.lock' objects}
        1    0.000    0.000    0.000    0.000 random.py:771(SystemRandom)
       20    0.000    0.000    0.000    0.000 {built-in method _thread.get_ident}
       22    0.000    0.000    0.000    0.000 {built-in method posix.fspath}
        4    0.000    0.000    0.000    0.000 {built-in method _imp.exec_dynamic}
       10    0.000    0.000    0.000    0.000 {built-in method _imp.is_frozen}
       26    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:40(_relax_case)
        1    0.000    0.000    0.000    0.000 graph.py:13(Graph)
       14    0.000    0.000    0.000    0.000 {built-in method from_bytes}
       10    0.000    0.000    0.000    0.000 {method 'pop' of 'dict' objects}
        1    0.000    0.000    0.000    0.000 input.py:1(<module>)
        6    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:946(__init__)
        1    0.000    0.000    0.000    0.000 random.py:218(__init_subclass__)
        1    0.000    0.000    0.000    0.000 _bootlocale.py:33(getpreferredencoding)
        4    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:1095(__init__)
        1    0.000    0.000    0.000    0.000 {built-in method _locale.nl_langinfo}
        1    0.000    0.000    0.000    0.000 codecs.py:309(__init__)
        6    0.000    0.000    0.000    0.000 {built-in method _imp._fix_co_filename}
       10    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:406(has_location)
        2    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:561(_validate_hash_pyc)
        1    0.000    0.000    0.000    0.000 {built-in method posix.register_at_fork}
        1    0.000    0.000    0.000    0.000 graph.py:2(<module>)
        1    0.000    0.000    0.000    0.000 random.py:117(__init__)
        6    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:971(get_filename)
        2    0.000    0.000    0.000    0.000 {built-in method math.log}
        1    0.000    0.000    0.000    0.000 input.py:68(ReadInput)
        1    0.000    0.000    0.000    0.000 codecs.py:260(__init__)
        1    0.000    0.000    0.000    0.000 graph.py:2(Vertice)
        6    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:781(create_module)
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
        1    0.000    0.000    0.000    0.000 {built-in method math.sqrt}


