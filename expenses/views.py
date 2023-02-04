from django.views.generic.list import ListView

from .forms import ExpenseSearchForm
from .models import Expense, Category
from .reports import summary_per_category
from django.shortcuts import render, redirect


class ExpenseListView(ListView):
    model = Expense
    paginate_by = 5

    def get_context_data(self, *, object_list=None, **kwargs):
        queryset = object_list if object_list is not None else self.object_list

        form = ExpenseSearchForm(self.request.GET)
        if form.is_valid():
            name = form.cleaned_data.get("name", "").strip()
            if name:
                queryset = queryset.filter(name__icontains=name)

            category = form.cleaned_data["category"]
            if category:
                queryset = queryset.filter(category=category)

        return super().get_context_data(
            form=form,
            object_list=queryset,
            summary_per_category=summary_per_category(queryset),
            **kwargs
        )

    def date_request(request):
        if request.method == "POST":
            fromdate = request.POST.get("fromdate")
            todate = request.POST.get("todate")
            searchresult = Expense.objects.ordering("-fromdate")
            return render(request, "expense-list", {"data": searchresult})


class CategoryListView(ListView):
    model = Category
    paginate_by = 5
