#include "lists.h"

/**
 * check_cycle - checks if a linked list contains a cycle
 * @list: linked list to check
 *
 * Return: 1 if the list has a cycle, 0 if it doesn't
 */

int check_cycle(listint_t *list)
{
	listint_t *held, *current;
	int flag = 0;

	if (list)
	{
		held = list;
		while (held && flag == 0)
		{
			current = held->next;
			while (current)
			{
				if (current == held)
				{
					flag = 1;
					break;
				}
				current = current->next;
			}
			held = held->next;
		}
	}
	return (flag);
}
