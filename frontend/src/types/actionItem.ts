export interface Task {
    id: number;
    title: string;
    priority: "High" | "Medium" | "Low";
    status: "Pending" | "Completed";
    due_date?: string | null;
}

export interface HCPActionGroup {
    hcp: {
        id: number;
        name: string;
        hospital: string;
    };

    pending: number;
    completed: number;

    tasks: Task[];
}