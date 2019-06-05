/* TEMPLATE GENERATED TESTCASE FILE
Filename: CWE415_Double_Free__malloc_free_long_84_goodG2B.cpp
Label Definition File: CWE415_Double_Free__malloc_free.label.xml
Template File: sources-sinks-84_goodG2B.tmpl.cpp
*/
/*
 * @description
 * CWE: 415 Double Free
 * BadSource:  Allocate data using malloc() and Deallocate data using free()
 * GoodSource: Allocate data using malloc()
 * Sinks:
 *    GoodSink: do nothing
 *    BadSink : Deallocate data using free()
 * Flow Variant: 84 Data flow: data passed to class constructor and destructor by declaring the class object on the heap and deleting it after use
 *
 * */
#ifndef OMITGOOD

#include "std_testcase.h"
#include "CWE415_Double_Free__malloc_free_long_84.h"

namespace CWE415_Double_Free__malloc_free_long_84
{
CWE415_Double_Free__malloc_free_long_84_goodG2B::CWE415_Double_Free__malloc_free_long_84_goodG2B(long * dataCopy)
{
    data = dataCopy;
    data = (long *)malloc(100*sizeof(long));
    /* FIX: Do NOT free data in the source - the bad sink frees data */
}

CWE415_Double_Free__malloc_free_long_84_goodG2B::~CWE415_Double_Free__malloc_free_long_84_goodG2B()
{
    /* POTENTIAL FLAW: Possibly freeing memory twice */
    free(data);
}
}
#endif /* OMITGOOD */
